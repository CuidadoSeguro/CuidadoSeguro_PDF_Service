from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional

from app.services.pdf_service import generar_pdf


router = APIRouter()


class DatosPDF(BaseModel):
    rut: str
    nombre: str
    fecha_nacimiento: str
    tipo_documento: str

@router.post("/api/pdf/generar")
def generar_documento(datos: DatosPDF):
    pdf = generar_pdf(datos.model_dump())

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
                'attachment; filename="documento_cuidado_seguro.pdf"'
        }
    )
