import pandas as pd

class ABCAnalysis:

    def __init__(self, productos):

        self.df = productos.copy()

    def classify(self):

        df = self.df.copy()

        df = df.sort_values(
            "Venta",
            ascending=False
        )

        total = df["Venta"].sum()

        df["Pct"] = (
            df["Venta"] /
            total
        ) * 100

        df["Acumulado"] = (
            df["Pct"]
            .cumsum()
        )

        def categoria(x):

            if x <= 80:
                return "A"

            if x <= 95:
                return "B"

            return "C"

        df["Clase"] = (
            df["Acumulado"]
            .apply(categoria)
        )

        return df