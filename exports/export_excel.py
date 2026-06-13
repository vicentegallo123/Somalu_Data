import os
import pandas as pd


class ExcelExporter:

    @staticmethod
    def export(df, nombre):

        os.makedirs(
            "exports",
            exist_ok=True
        )

        archivo = f"exports/{nombre}.xlsx"

        df.to_excel(
            archivo,
            index=False
        )

        return archivo