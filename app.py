import streamlit as st
import pandas as pd

from services.loader import DataLoader
from services.kpis import KPIService
from services.analytics import AnalyticsService
from services.forecasting import ForecastService
from services.discounts import DiscountService
from services.inventory import InventoryService  

from exports.export import ExportService
from components.sales_cards import draw_metric
from components.charts import Charts
from components.tables import Tables

st.set_page_config(
    page_title="SOMALU Analytics",
    layout="wide"
)

st.title("📊 Dashboard SOMALU")

# CARGE
data = DataLoader.load_all()

ventas = data["ventas"]
productos = data["productos"]
productos_periodo = data["productos_periodo"]
inventario = data["inventario"]  

# INIT
kpi = KPIService(ventas)
analytics = AnalyticsService(ventas)
peor_dia = analytics.dia_menos_ventas_sin_lunes()
mejor_dia = analytics.dia_mas_ventas_sin_lunes()
discounts = DiscountService(ventas)

# Servicio de inventario y alertas
inventory_service = InventoryService(inventario, productos_periodo)
alertas_stock = inventory_service.alertas_reabastecimiento(dias_minimos=5)

# ta
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Resumen",
    "Ventas",
    "Productos",
    "Forecast",
    "Inventario"
])

with tab1:

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success(
            f" Día con más ventas: "
            f"{mejor_dia['DIA_SEMANA']} "
            f"(${mejor_dia['TOTAL']:,.2f})"
        )

    with c2:
        st.warning(
            f" Día con menos ventas: "
            f"{peor_dia['DIA_SEMANA']} "
            f"(${peor_dia['TOTAL']:,.2f})"
        )

    with c3:
        draw_metric(
            "Ticket Promedio",
            f"${kpi.ticket_promedio():,.2f}"
        )

    with c4:
        draw_metric(
            "% Descuento",
            f"{kpi.porcentaje_descuento():.2f}%"
        )

with tab2:

    ventas_mes = analytics.ventas_por_mes()

    st.plotly_chart(
        Charts.ventas_mensuales(
            ventas_mes
        ),
        use_container_width=True
    )

    ventas_semana = analytics.ventas_por_dia_semana()

    st.plotly_chart(
        Charts.ventas_dia_semana(
            ventas_semana
        ),
        use_container_width=True
    )

    heatmap = analytics.heatmap_mes_dia()

    st.plotly_chart(
        Charts.heatmap(
            heatmap
        ),
        use_container_width=True
    )

with tab3:

    st.subheader(
        "Productos Vendidos"
    )

    Tables.top_productos(
        productos_periodo
    )

with tab4:

    forecast_service = (
        ForecastService(ventas)
    )

    model, forecast = (
        forecast_service.forecast_30_dias()
    )

    st.plotly_chart(
        Charts.forecast(
            forecast
        ),
        use_container_width=True
    )


with tab5:
    st.subheader("📦 Inventory Status")
    
    # Financial KPI cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Items", len(inventario))
    col2.error(f"🚨 Critical Stock: {len(alertas_stock)}")
    col3.metric("Total Inventory Value", f"${inventario['COSTO_TOTAL'].sum():,.2f}")

    # Financial analysis by department
    st.subheader("📊 Investment by Department")
    resumen = inventory_service.resumen_por_categoria()
    st.dataframe(resumen, use_container_width=True)
    
    # Visual investment distribution
    import plotly.express as px
    fig = px.pie(resumen, values='COSTO_TOTAL', names='CATEGORIA', title="Investment per Category")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------
# dowloads
# -----------------------------------------------------
st.markdown("---")

csv = ventas.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Descargar datos de ventas en CSV",
    data=csv,
    file_name='ventas_somalu.csv',
    mime='text/csv',
)

datos_resumen = pd.DataFrame({
    "Métrica": ["Ventas Totales", "Promedio Diario", "Ticket Promedio", "% Descuento"],
    "Valor": [kpi.ventas_totales(), kpi.promedio_diario(), kpi.ticket_promedio(), kpi.porcentaje_descuento()]
})


st.download_button(
    label="📥 Descargar Resumen en Excel",
    data=ExportService.to_excel(datos_resumen),
    file_name="reporte_somalu.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


texto_pdf = f"Ventas Totales: ${kpi.ventas_totales():,.2f} | Ticket Promedio: ${kpi.ticket_promedio():,.2f}"
st.download_button(
    label="📥 Descargar Resumen en PDF",
    data=ExportService.to_pdf(texto_pdf),
    file_name="reporte_somalu.pdf",
    mime="application/pdf"
)