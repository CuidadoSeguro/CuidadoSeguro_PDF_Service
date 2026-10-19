from fastapi import FastAPI

from app.routes.pdf_routes import router as pdf_router

app = FastAPI(
    title="Cuidado Seguro - PDF Service",
    description="Microservicio para generación de documentos PDF de Cuidado Seguro",
    version="1.0.0"
)

app.include_router(pdf_router)


@app.get("/")
def inicio():
    return {
        "mensaje": "Cuidado Seguro PDF Service funcionando",
        "version": "1.0.0"
    }