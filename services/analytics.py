import pandas as pd

class AnalyticsService:
    def __init__(self, ventas):
        self.df = ventas.copy()
        self.df["FECHA"] = pd.to_datetime(self.df["FECHA"], errors="coerce")
        self.df = self.df.dropna(subset=["FECHA"])
        self.df["MES"] = self.df["FECHA"].dt.month_name()
        self.df["DIA"] = self.df["FECHA"].dt.day
        self.df["DIA_SEMANA"] = self.df["FECHA"].dt.day_name()

    def ventas_por_mes(self):
        return self.df.groupby("MES")["TOTAL"].sum().reset_index()

    def ventas_por_dia(self):
        return self.df.groupby("FECHA")["TOTAL"].sum().reset_index()

    def ventas_por_dia_semana(self):
        orden = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        resultado = self.df.groupby("DIA_SEMANA")["TOTAL"].sum().reset_index()
        resultado["DIA_SEMANA"] = pd.Categorical(resultado["DIA_SEMANA"], categories=orden, ordered=True)
        return resultado.sort_values("DIA_SEMANA")

    def heatmap_mes_dia(self):
        return self.df.pivot_table(values="TOTAL", index="MES", columns="DIA", aggfunc="sum", fill_value=0)

    def dia_menos_ventas_sin_lunes(self):
        df = self.df[self.df["DIA_SEMANA"] != "Monday"]
        resumen = df.groupby("DIA_SEMANA")["TOTAL"].mean().reset_index()
        return resumen.loc[resumen["TOTAL"].idxmin()]

    def dia_mas_ventas_sin_lunes(self):
        df = self.df[self.df["DIA_SEMANA"] != "Monday"]
        resumen = df.groupby("DIA_SEMANA")["TOTAL"].mean().reset_index()
        return resumen.loc[resumen["TOTAL"].idxmax()]

    def mejor_dia_por_mes(self):
        resumen = self.df.groupby(["MES", "FECHA"])["TOTAL"].sum().reset_index()
        idx = resumen.groupby("MES")["TOTAL"].idxmax()
        return resumen.loc[idx]

    def peor_dia_por_mes(self):
        resumen = self.df.groupby(["MES", "FECHA"])["TOTAL"].sum().reset_index()
        idx = resumen.groupby("MES")["TOTAL"].idxmin()
        return resumen.loc[idx]