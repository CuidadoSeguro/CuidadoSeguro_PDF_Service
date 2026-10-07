# CuidadoSeguro_PDF_Service

Microservicio desarrollado en **Python** para la generación de documentos PDF del sistema **Cuidado Seguro**.

Este microservicio forma parte de la arquitectura de microservicios de Cuidado Seguro y tiene como responsabilidad generar documentos PDF a partir de información proporcionada por otros servicios de la plataforma.

---

## 📋 Descripción

**Cuidado Seguro - PDF Service** es un microservicio desarrollado con **FastAPI** y **Python**, orientado a la generación de documentos PDF.

Actualmente permite recibir información mediante una API REST y generar un documento PDF utilizando la biblioteca **ReportLab**.

El servicio está diseñado siguiendo una arquitectura separada por responsabilidades:

```text
Cliente / Frontend
       │
       ▼
FastAPI
       │
       ▼
Routes
       │
       ▼
Services
       │
       ▼
ReportLab
       │
       ▼
Documento PDF

🎯 Objetivo
El objetivo principal del microservicio es centralizar la generación de documentos PDF utilizados por la plataforma Cuidado Seguro.
Entre sus funcionalidades proyectadas se encuentran:
- Generación de listados de pacientes.
- Generación de documentos clínicos.
- Generación de informes.
- Generación de fichas y reportes.
- Descarga de documentos PDF.
- Integración con los demás microservicios de Cuidado Seguro.

🛠️ Tecnologías utilizadas
Tecnología	Uso
Python	Lenguaje de programación
FastAPI	Framework para desarrollo de API REST
Uvicorn	Servidor ASGI
ReportLab	Generación de documentos PDF
Pydantic	Validación de datos
Git	Control de versiones
GitHub	Repositorio del proyecto

📁 Estructura del proyecto
CuidadoSeguro_PDF_Service/
│
├── app/
│   ├── routes/
│   │   └── pdf_routes.py
│   │
│   ├── services/
│   │   └── pdf_service.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── .venv/

Descripción de los componentes
app/main.py
Archivo principal de la aplicación FastAPI.
Se encarga de:
- Inicializar FastAPI.
- Configurar el nombre del servicio.
- Configurar la descripción.
- Configurar la versión.
- Registrar las rutas del microservicio.
app/routes/pdf_routes.py
Contiene los endpoints relacionados con la generación de documentos PDF.
Actualmente dispone del endpoint:
POST /api/pdf/generar

app/services/pdf_service.py
Contiene la lógica encargada de generar los documentos PDF mediante ReportLab.
La separación entre rutas y servicios permite mantener una arquitectura organizada y facilitar el mantenimiento del proyecto.

🚀 Instalación
1. Clonar el repositorio
git clone https://github.com/CuidadoSeguro/CuidadoSeguro_PDF_Service.git

Ingresar al proyecto:
cd CuidadoSeguro_PDF_Service

2. Crear entorno virtual
En Windows:
python -m venv .venv

Activar el entorno virtual:
.\.venv\Scripts\Activate.ps1

Si el entorno está activo, la terminal mostrará:
(.venv)

3. Instalar dependencias
pip install -r requirements.txt

▶️ Ejecutar el microservicio
Con el entorno virtual activado:
uvicorn app.main:app --reload

El servicio estará disponible en:
http://127.0.0.1:8000

📚 Documentación de la API
FastAPI genera automáticamente la documentación interactiva mediante Swagger.
Acceder a:
http://127.0.0.1:8000/docs

También se encuentra disponible la especificación OpenAPI en:
http://127.0.0.1:8000/openapi.json

🔌 Endpoints
Estado del servicio
GET /

Respuesta:
{
  "mensaje": "Cuidado Seguro PDF Service funcionando",
  "version": "1.0.0"
}

Generar PDF
POST /api/pdf/generar

Este endpoint recibe información mediante JSON y genera un documento PDF.
Request
Actualmente recibe:
{
  "rut": "12.345.678-9",
  "nombre": "Juan Pérez",
  "fecha_nacimiento": "1980-05-15",
  "tipo_documento": "Ficha Clínica"
}

Response
Cuando la operación es exitosa:
HTTP 200 OK

El servicio devuelve un archivo:
documento_cuidado_seguro.pdf

con el tipo de contenido:
application/pdf

🧪 Pruebas
El endpoint puede probarse directamente desde Swagger:
http://127.0.0.1:8000/docs

Seleccionar:
POST /api/pdf/generar

Luego:
1. Seleccionar Try it out.
2. Ingresar los datos JSON.
3. Presionar Execute.
4. Verificar que la respuesta sea 200.
5. Descargar el archivo PDF generado.
🌿 Estrategia de ramas
El proyecto utiliza una estrategia de desarrollo basada en ramas.
La rama principal es:
main

El desarrollo actual se realiza en:
feature/pdf-service

La metodología utilizada es:
main
 │
 └── feature/pdf-service
          │
          ├── Desarrollo
          ├── Pruebas
          └── Validación
                  │
                  ▼
             Pull Request
                  │
                  ▼
                main

Los cambios no se incorporan directamente a main hasta que hayan sido desarrollados y probados correctamente.
📦 Dependencias
Las principales dependencias del proyecto son:
- FastAPI
- Uvicorn
- ReportLab
- Pydantic
Las versiones utilizadas se encuentran especificadas en:
requirements.txt

🔐 Seguridad
El microservicio está diseñado para integrarse posteriormente con los mecanismos de seguridad utilizados por Cuidado Seguro.
Entre las funcionalidades de seguridad proyectadas se encuentran:
- Autenticación mediante JWT.
- Validación de tokens.
- Integración con API Gateway.
- Control de acceso según roles.
- Comunicación segura mediante HTTPS.
- Protección de información clínica.
La implementación de estas funcionalidades se realizará durante las siguientes etapas del proyecto.
☁️ Integración con Cuidado Seguro
El microservicio PDF está diseñado para integrarse con la arquitectura general de Cuidado Seguro.
Arquitectura proyectada:
                    CUIDADO SEGURO
                          │
                          ▼
                     Frontend
                    Angular / React
                          │
                          ▼
                     API Gateway
                          │
             ┌────────────┼─────────────┐
             │            │             │
             ▼            ▼             ▼
        Auth Service  Pacientes      PDF Service
                       Service        Python
                                         │
                                         ▼
                                      ReportLab
                                         │
                                         ▼
                                         PDF

El PDF Service tendrá como responsabilidad exclusiva la generación de documentos, evitando mezclar esta lógica con los demás microservicios.
📄 Funcionalidades futuras
Se contempla ampliar el microservicio para generar:
- [ ] Listado de pacientes.
- [ ] Listado de pacientes filtrado.
- [ ] Informes de pacientes.
- [ ] Ficha clínica en PDF.
- [ ] Reportes de signos vitales.
- [ ] Reportes de antropometría.
- [ ] Historial de evoluciones.
- [ ] Documentos clínicos completos.
- [ ] Integración con pacientes-service.
- [ ] Integración con API Gateway.
- [ ] Autenticación JWT.
- [ ] Integración con frontend administrativo.
👨‍💻 Proyecto
Cuidado Seguro
Microservicio:
CuidadoSeguro_PDF_Service
Tecnología principal:
Python + FastAPI + ReportLab
Estado actual:
En desarrollo
Rama actual:
feature/pdf-service

📌 Estado del proyecto
Actualmente se encuentra implementado:
- ✅ Proyecto Python.
- ✅ Entorno virtual.
- ✅ FastAPI.
- ✅ Uvicorn.
- ✅ ReportLab.
- ✅ Endpoint de estado.
- ✅ Endpoint de generación de PDF.
- ✅ Documentación Swagger.
- ✅ Generación real de archivos PDF.
- ✅ Descarga del PDF desde Swagger.
- ⏳ Generación de listado de múltiples pacientes.
- ⏳ Integración con pacientes-service.
- ⏳ Integración con API Gateway.
- ⏳ Integración con frontend.
- ⏳ Seguridad JWT.
📜 Licencia
Proyecto académico y de desarrollo perteneciente a Cuidado Seguro.

### Una decisión que te recomiendo

Yo **sí pondría este README ahora**, antes de continuar con el listado de pacientes. Así nuestro repositorio ya queda documentado desde el inicio y después solo vamos actualizando las secciones de **funcionalidades**, **endpoints** y **estado del proyecto**.

Si quieres, en el siguiente paso podemos crear directamente este `README.md` dentro de tu proyecto y dejarlo listo para hacer el **commit en `feature/pdf-service`**.






    






























Esfuerzo de razonamientoGPT-5.6 Sol

  




































    To pick up a draggable item, press the space bar.
    While dragging, use the arrow keys to move the item.
    Press space again to drop the item in its new position, or press escape to cancel.
  








  




Arrastra para reordenar los elementos de navegación anclados



