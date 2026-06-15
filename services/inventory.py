import pandas as pd

class InventoryService:
    def __init__(self, inventario_df, productos_df):
        self.inv = inventario_df.copy()
        self.productos = productos_df.copy() 
        # Safety check: if columns are not standardized, fix them now
        self._self_heal()

    def _self_heal(self):
        """Ensures 'DESCRIPCION' column exists in both dataframes."""
        if 'DESCRIPCION' not in self.inv.columns and 'PRODUCTO' in self.inv.columns:
            self.inv.rename(columns={'PRODUCTO': 'DESCRIPCION'}, inplace=True)
            
        if 'DESCRIPCION' not in self.productos.columns and 'PRODUCTO' in self.productos.columns:
            self.productos.rename(columns={'PRODUCTO': 'DESCRIPCION'}, inplace=True)

    def calcular_cobertura(self, dias_periodo=30):
        # Safety check: ensure column exists
        if 'DESCRIPCION' not in self.productos.columns:
            print(f"DEBUG ERROR: 'DESCRIPCION' not found in: {self.productos.columns}")
            return pd.DataFrame()

        # Group by the standardized column
        ventas_totales = self.productos.groupby('DESCRIPCION')['CANTIDAD'].sum().reset_index()
        ventas_totales['Venta_Diaria_Promedio'] = ventas_totales['CANTIDAD'] / dias_periodo
        
        # Merge using the standardized column
        df_analisis = pd.merge(self.inv, ventas_totales[['DESCRIPCION', 'Venta_Diaria_Promedio']], 
                               on='DESCRIPCION', how='left')
        
        df_analisis['Venta_Diaria_Promedio'] = df_analisis['Venta_Diaria_Promedio'].fillna(0)

        # Calculate remaining days
        df_analisis['Dias_Restantes'] = df_analisis.apply(
            lambda x: x['STOCK_ACTUAL'] / x['Venta_Diaria_Promedio'] if x['Venta_Diaria_Promedio'] > 0 else 999, 
            axis=1
        )
        return df_analisis

    def resumen_por_categoria(self):
        return self.inv.groupby('CATEGORIA').agg({
            'STOCK_ACTUAL': 'sum',
            'COSTO_TOTAL': 'sum'
        }).reset_index()

    def alertas_reabastecimiento(self, dias_minimos=7):
        df = self.calcular_cobertura()
        if not df.empty and 'Dias_Restantes' in df.columns:
            return df[df['Dias_Restantes'] <= dias_minimos].sort_values('Dias_Restantes')
        return df