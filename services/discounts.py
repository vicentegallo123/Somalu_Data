class DiscountService:
    
    def __init__(self, ventas):
        self.df = ventas.copy()

    def total_descuentos(self):
        return self.df["Descuentos"].sum()

    def top_descuentos(self):

        return (
            self.df
            .sort_values(
                "Descuentos",
                ascending=False
            )
            .head(10)
        )

    def porcentaje_descuento(self):

        ventas = self.df["Total"].sum()

        descuentos = (
            self.df["Descuentos"]
            .sum()
        )

        if ventas == 0:
            return 0

        return (
            descuentos /
            ventas
        ) * 100