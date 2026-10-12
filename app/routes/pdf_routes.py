from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.services.pdf_service import generar_pdf


router = APIRouter(
    prefix="/api/pdf",
    tags=["PDF"]
)


class DatosPDF(BaseModel):
    rut: str
    nombre: str
    fecha_nacimiento: str
    tipo_documento: str


@router.post("/generar")
def generar_documento_pdf(datos: DatosPDF):

    pdf = generar_pdf(datos.model_dump())
    pdf.seek(0)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=documento_cuidado_seguro.pdf"
        }
    )