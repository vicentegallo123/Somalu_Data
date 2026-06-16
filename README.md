📊 SOMALU Data Analytics PlatformPlataforma avanzada para el análisis de ventas, visualización de KPIs y pronóstico (forecasting) de inventario basada en Streamlit.🏗️ Arquitectura del SistemaEl sistema está diseñado bajo un modelo modular que separa la interfaz de usuario de la lógica de análisis de datos.Fragmento de códigograph TD

    A[app.py - Dashboard Streamlit] --> B[components/ - UI]
    A --> C[services/ - Lógica de Negocio]
    C --> D[analytics.py]
    C --> E[forecasting.py]
    C --> F[inventory.py]
    D & E & F --> G[data/ - Fuentes de Datos]
    
📁 Estructura del ProyectoPlaintextSOMALU_Data/

├── app.py                ← Punto de entrada de la App (Streamlit)
├── requirements.txt      ← Dependencias del sistema
├── data/                 ← Fuente de datos (.xlsx, .xls)
├── exports/              ← Reportes generados
├── components/           ← Módulos de visualización (charts, cards, tables)
└── services/             ← Capa lógica de análisis:
    ├── analytics.py      ← Procesamiento y KPIs
    ├── forecasting.py    ← Modelos predictivos (Prophet)
    ├── inventory.py      ← Gestión de stock y reabastecimiento
    └── loader.py         ← Normalización de datos en inglés/español
    
🚀 Instalación y Ejecución1. RequisitosBashpip install -r requirements.txt

2. EjecuciónPara iniciar el dashboard interactivo:Bashpython -m streamlit run app.py
   
🛠️ Tecnologías UtilizadasCategoríaTecnologíasDashboardsStreamlit, Plotly, Seaborn, MatplotlibAnálisisPandas, NumPy, Scikit-learn, ProphetReportesReportLab, XlsxWriter🧠 Características Principales
📈 Análisis PredictivoGracias al motor de Facebook Prophet, el sistema es capaz de analizar el histórico de ventas en tus archivos de Excel y proyectar la demanda futura.
⚙️ Normalización InteligenteEl módulo loader.py mapea automáticamente columnas de reportes en inglés (ej. Product, Quantity) a español para que tu lógica de análisis funcione de manera uniforme sin importar el proveedor del reporte.
📋 Gestión de KPIsSales Cards: Visualización inmediata de ventas totales y márgenes.Forecasting: Proyecciones a 30, 60 y 90 días.Inventory Alerts: Identificación de productos con riesgo de agotamiento (Stockout Risk).
