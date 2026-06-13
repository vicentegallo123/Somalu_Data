import pandas as pd


class KPIService:

    def __init__(self, ventas):
        self.df = ventas.copy()

    def ventas_totales(self):
        return self.df["TOTAL"].sum()

    def promedio_diario(self):
        return self.df["TOTAL"].mean()

    def max_venta(self):
        return self.df["TOTAL"].max()

    def min_venta(self):
        return self.df["TOTAL"].min()

    def mejor_dia(self):
        fila = self.df.loc[
            self.df["TOTAL"].idxmax()
        ]
        return fila

    def peor_dia(self):
        fila = self.df.loc[
            self.df["TOTAL"].idxmin()
        ]
        return fila

    def ticket_promedio(self):
        return self.df[
            "PROMEDIO_POR_CUENTAS"
        ].mean()

    def promedio_personas(self):
        return self.df[
            "PROMEDIO_POR_PERSONAS"
        ].mean()

    def total_descuentos(self):
        return self.df[
            "DESCUENTOS"
        ].sum()

    def porcentaje_descuento(self):

        ventas = self.ventas_totales()

        if ventas == 0:
            return 0

        return (
            self.total_descuentos()
            / ventas
        ) * 100