import pandas as pd


class DataLoader:

    @staticmethod
    def load_excel(path):

        try:

            df = pd.read_excel(
                path,
                header=4
            )

            df.columns = (
                df.columns
                .astype(str)
                .str.strip()
                .str.upper()
            )

            return df

        except Exception as e:

            print(f"Error leyendo {path}: {e}")

            return pd.DataFrame()

    @staticmethod
    def load_all():

        return {
            "ventas": DataLoader.load_excel(
                "data/VENTASXDIA.XLS"
            ),
            "productos": DataLoader.load_excel(
                "data/PRODUCTOS.XLS"
            ),
            "productos_periodo": DataLoader.load_excel(
                "data/PRODUCTOSVENDIDOSPERIODO.XLS"
            ),
        }