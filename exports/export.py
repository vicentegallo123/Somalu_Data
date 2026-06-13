import pandas as pd
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class ExportService:
    @staticmethod
    def to_excel(df):
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        buffer.seek(0)
        return buffer

    @staticmethod
    def to_pdf(texto_resumen):
        buffer = io.BytesIO()
        pdf = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()
        elementos = [
            Paragraph("Reporte SOMALU", styles["Title"]),
            Spacer(1, 20),
            Paragraph(texto_resumen, styles["BodyText"])
        ]
        pdf.build(elementos)
        buffer.seek(0)
        return buffer