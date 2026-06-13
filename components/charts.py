import plotly.express as px
import plotly.graph_objects as go


class Charts:

    @staticmethod
    def ventas_mensuales(df):

        fig = px.line(
            df,
            x="MES",
            y="TOTAL",
            markers=True,
            title="Ventas por Mes"
        )

        fig.update_layout(
            height=500
        )

        return fig

    @staticmethod
    def ventas_dia_semana(df):

        fig = px.bar(
            df,
            x="DIA_SEMANA",
            y="TOTAL",
            title="Ventas por Día de Semana"
        )

        return fig

    @staticmethod
    def top_productos(df):

  
        fig = px.bar(
            df,
            x="CANTIDAD",
            y="DESCRIPCION",
            orientation="h",
            title="Top Productos"
        )

        return fig

    @staticmethod
    def descuentos(df):

        fig = px.bar(
            df,
            x="DESCUENTOS",
            y="FECHA",
            orientation="h",
            title="Top Descuentos"
        )

        return fig

    @staticmethod
    def heatmap(pivot):

        fig = px.imshow(
            pivot,
            aspect="auto",
            title="Heatmap de Ventas"
        )

        return fig

    @staticmethod
    def forecast(forecast):

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=forecast["ds"],
                y=forecast["yhat"],
                mode="lines",
                name="Predicción"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=forecast["ds"],
                y=forecast["yhat_upper"],
                mode="lines",
                name="Máximo"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=forecast["ds"],
                y=forecast["yhat_lower"],
                mode="lines",
                name="Mínimo"
            )
        )

        return fig