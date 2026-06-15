import pandas as pd

class DataLoader:
    @staticmethod
    def _standardize_columns(df):
        """Standardizes headers to ensure 'DESCRIPCION' and 'STOCK_ACTUAL' exist."""
        # Clean column names (remove spaces, convert to uppercase)
        df.columns = df.columns.astype(str).str.strip().str.upper()
        
        # Mapping Excel headers to your system standard
        rename_map = {
            'PRODUCTO': 'DESCRIPCION',
            'CANTIDAD ACTUAL': 'STOCK_ACTUAL',
            'COSTO UNIDAD': 'COSTO_UNITARIO',
            'TOTAL COSTO': 'COSTO_TOTAL'
        }
        df.rename(columns=rename_map, inplace=True)
        return df

    @staticmethod
    def load_excel(path, header_row=4):
        try:
            df = pd.read_excel(path, header=header_row)
            return DataLoader._standardize_columns(df)
        except Exception as e:
            print(f"Error loading {path}: {e}")
            return pd.DataFrame()

    @staticmethod
    def load_inventario(path):
        try:
            # Load all sheets from the Excel file
            diccionario_hojas = pd.read_excel(path, sheet_name=None, header=2)
            df_list = []
            
            for nombre_hoja, df in diccionario_hojas.items():
                df = DataLoader._standardize_columns(df)
                df['CATEGORIA'] = nombre_hoja 
                df_list.append(df)
            
            # Combine all sheets
            inventario = pd.concat(df_list, ignore_index=True)
            
            # Ensure numeric integrity
            inventario['STOCK_ACTUAL'] = pd.to_numeric(inventario.get('STOCK_ACTUAL', 0), errors='coerce').fillna(0)
            
            return inventario
        except Exception as e:
            print(f"Error loading consolidated inventory: {e}")
            return pd.DataFrame()

    @staticmethod
    def load_all():
        return {
            "ventas": DataLoader.load_excel("data/VENTASXDIA.XLS"),
            "productos": DataLoader.load_excel("data/PRODUCTOS.XLS"),
            "productos_periodo": DataLoader.load_excel("data/PRODUCTOSVENDIDOSPERIODO.XLS"),
            "inventario": DataLoader.load_inventario("data/inventario.xlsx")
        }