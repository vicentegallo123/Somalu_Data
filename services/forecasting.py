from prophet import Prophet
import pandas as pd


class ForecastService:

    def __init__(self, ventas):
        self.df = ventas.copy()

    def forecast_30_dias(self):

        prophet_df = self.df[
            ["FECHA", "TOTAL"]
        ].copy()

        prophet_df["FECHA"] = pd.to_datetime(
            prophet_df["FECHA"],
            errors="coerce"
        )

        prophet_df["TOTAL"] = pd.to_numeric(
            prophet_df["TOTAL"],
            errors="coerce"
        )

        prophet_df = prophet_df.dropna()

        prophet_df.columns = [
            "ds",
            "y"
        ]

        model = Prophet()

        model.fit(prophet_df)

        future = model.make_future_dataframe(
            periods=30
        )

        forecast = model.predict(future)

        return model, forecast