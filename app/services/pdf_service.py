from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER


def generar_pdf(datos: dict) -> BytesIO:
    """
    Genera un documento PDF con los datos proporcionados.

    Args:
        datos: Diccionario con la información del paciente/documento.

    Returns:
        BytesIO: Archivo PDF generado en memoria.
    """

    buffer = BytesIO()

    documento = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    estilos = getSampleStyleSheet()

    titulo = estilos["Title"]
    titulo.alignment = TA_CENTER

    normal = estilos["Normal"]

    contenido = []

    contenido.append(
        Paragraph("CUIDADO SEGURO", titulo)
    )

    contenido.append(
        Spacer(1, 20)
    )

    contenido.append(
        Paragraph(
            "Documento generado por Cuidado Seguro",
            normal
        )
    )

    contenido.append(
        Spacer(1, 20)
    )

    contenido.append(
        Paragraph(
            f"<b>RUT:</b> {datos.get('rut', '')}",
            normal
        )
    )

    contenido.append(
        Paragraph(
            f"<b>Nombre:</b> {datos.get('nombre', '')}",
            normal
        )
    )

    contenido.append(
        Paragraph(
            f"<b>Fecha de nacimiento:</b> "
            f"{datos.get('fecha_nacimiento', '')}",
            normal
        )
    )

    contenido.append(
        Paragraph(
            f"<b>Tipo de documento:</b> "
            f"{datos.get('tipo_documento', '')}",
            normal
        )
    )

    documento.build(contenido)

    buffer.seek(0)

    return buffer