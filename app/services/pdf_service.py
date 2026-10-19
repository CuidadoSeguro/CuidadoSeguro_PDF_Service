
from io import BytesIO
from datetime import datetime
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable
)


# Paleta institucional
AZUL_OSCURO = colors.HexColor("#163A5F")
AZUL = colors.HexColor("#247BA0")
AZUL_CLARO = colors.HexColor("#EAF3F8")
GRIS_FONDO = colors.HexColor("#F5F7FA")
GRIS_TEXTO = colors.HexColor("#526273")
GRIS_BORDE = colors.HexColor("#D9E2EA")
BLANCO = colors.white


def generar_pdf(datos: dict) -> BytesIO:
    """
    Genera un PDF institucional de Cuidado Seguro.

    Args:
        datos: Diccionario con los datos del paciente
               y del documento.

    Returns:
        BytesIO: Archivo PDF generado en memoria.
    """

    buffer = BytesIO()

    documento = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2.7 * cm,
        bottomMargin=2.2 * cm,
        title="Documento - Cuidado Seguro",
        author="Cuidado Seguro"
    )

    estilos = getSampleStyleSheet()

    # Estilos personalizados
    estilo_titulo = ParagraphStyle(
        "TituloInstitucional",
        parent=estilos["Title"],
        fontName="Helvetica-Bold",
        fontSize=23,
        leading=28,
        textColor=AZUL_OSCURO,
        alignment=TA_CENTER,
        spaceAfter=8
    )

    estilo_subtitulo = ParagraphStyle(
        "Subtitulo",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        textColor=GRIS_TEXTO,
        alignment=TA_CENTER
    )

    estilo_seccion = ParagraphStyle(
        "TituloSeccion",
        parent=estilos["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=AZUL_OSCURO,
        alignment=TA_LEFT,
        spaceBefore=8,
        spaceAfter=10
    )

    estilo_etiqueta = ParagraphStyle(
        "Etiqueta",
        parent=estilos["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=13,
        textColor=GRIS_TEXTO
    )

    estilo_valor = ParagraphStyle(
        "Valor",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=AZUL_OSCURO,
        wordWrap="LTR"
    )

    estilo_nota = ParagraphStyle(
        "Nota",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=12,
        textColor=GRIS_TEXTO
    )

    # Escapar los valores para evitar que caracteres como < o >
    # sean interpretados como etiquetas HTML por ReportLab.
    def obtener_valor(campo):
        valor = datos.get(campo)

        if valor is None or str(valor).strip() == "":
            return "No informado"

        return escape(str(valor).strip())

    contenido = []

    # Encabezado
    contenido.append(Spacer(1, 0.4 * cm))

    contenido.append(
        Paragraph("CUIDADO SEGURO", estilo_titulo)
    )

    contenido.append(
        Paragraph(
            "PLATAFORMA DE GESTIÓN DE INFORMACIÓN CLÍNICA",
            estilo_subtitulo
        )
    )

    contenido.append(Spacer(1, 0.5 * cm))

    contenido.append(
        HRFlowable(
            width="100%",
            thickness=2,
            color=AZUL,
            spaceBefore=4,
            spaceAfter=18
        )
    )

    # Título del documento
    contenido.append(
        Paragraph(
            "Ficha de identificación",
            estilo_seccion
        )
    )

    contenido.append(
        Paragraph(
            "Información de identificación del paciente "
            "y antecedentes del documento solicitado.",
            estilo_nota
        )
    )

    contenido.append(Spacer(1, 0.5 * cm))

    # Tabla de datos
    filas = [
        [
            Paragraph("IDENTIFICACIÓN", estilo_etiqueta),
            Paragraph("INFORMACIÓN", estilo_etiqueta)
        ],
        [
            Paragraph("RUT del paciente", estilo_etiqueta),
            Paragraph(obtener_valor("rut"), estilo_valor)
        ],
        [
            Paragraph("Nombre completo", estilo_etiqueta),
            Paragraph(obtener_valor("nombre"), estilo_valor)
        ],
        [
            Paragraph("Fecha de nacimiento", estilo_etiqueta),
            Paragraph(
                obtener_valor("fecha_nacimiento"),
                estilo_valor
            )
        ],
        [
            Paragraph("Tipo de documento", estilo_etiqueta),
            Paragraph(
                obtener_valor("tipo_documento"),
                estilo_valor
            )
        ]
    ]

    tabla = Table(
        filas,
        colWidths=[5.2 * cm, 11.1 * cm],
        repeatRows=1,
        hAlign="LEFT"
    )

    tabla.setStyle(
        TableStyle([
            # Encabezado
            ("BACKGROUND", (0, 0), (-1, 0), AZUL_OSCURO),
            ("TEXTCOLOR", (0, 0), (-1, 0), BLANCO),

            # Filas alternadas
            ("BACKGROUND", (0, 1), (-1, 1), GRIS_FONDO),
            ("BACKGROUND", (0, 2), (-1, 2), BLANCO),
            ("BACKGROUND", (0, 3), (-1, 3), GRIS_FONDO),
            ("BACKGROUND", (0, 4), (-1, 4), BLANCO),

            # Bordes y alineación
            ("BOX", (0, 0), (-1, -1), 0.8, GRIS_BORDE),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, GRIS_BORDE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            # Espaciado interno
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, -1), 13),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 13),
        ])
    )

    contenido.append(tabla)
    contenido.append(Spacer(1, 0.8 * cm))

    # Bloque informativo
    tipo_documento = obtener_valor("tipo_documento")

    bloque = Table(
        [[
            Paragraph(
                f"<b>Documento solicitado:</b><br/>"
                f"{tipo_documento}",
                estilo_valor
            )
        ]],
        colWidths=[16.3 * cm]
    )

    bloque.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), AZUL_CLARO),
            ("BOX", (0, 0), (-1, -1), 0.8, GRIS_BORDE),
            ("LINEBEFORE", (0, 0), (0, -1), 4, AZUL),
            ("LEFTPADDING", (0, 0), (-1, -1), 14),
            ("RIGHTPADDING", (0, 0), (-1, -1), 14),
            ("TOPPADDING", (0, 0), (-1, -1), 14),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ])
    )

    contenido.append(bloque)
    contenido.append(Spacer(1, 1 * cm))

    contenido.append(
        Paragraph(
            "Este documento ha sido generado mediante la "
            "plataforma Cuidado Seguro. La información debe "
            "ser verificada por el personal autorizado antes "
            "de su utilización.",
            estilo_nota
        )
    )

    # Encabezado y pie de página
    def dibujar_pagina(canvas, doc):
        canvas.saveState()

        ancho, alto = A4

        # Línea superior
        canvas.setStrokeColor(AZUL)
        canvas.setLineWidth(2)
        canvas.line(
            2 * cm,
            alto - 1.5 * cm,
            ancho - 2 * cm,
            alto - 1.5 * cm
        )

        # Pie de página
        canvas.setStrokeColor(GRIS_BORDE)
        canvas.setLineWidth(0.6)
        canvas.line(
            2 * cm,
            1.5 * cm,
            ancho - 2 * cm,
            1.5 * cm
        )

        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(GRIS_TEXTO)

        canvas.drawString(
            2 * cm,
            1.05 * cm,
            "Cuidado Seguro | Documento institucional"
        )

        canvas.drawRightString(
            ancho - 2 * cm,
            1.05 * cm,
            f"Página {doc.page}"
        )

        canvas.restoreState()

    documento.build(
        contenido,
        onFirstPage=dibujar_pagina,
        onLaterPages=dibujar_pagina
    )

    buffer.seek(0)

    return buffer
