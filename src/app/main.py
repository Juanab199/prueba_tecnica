from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

from app import SERVICE_VERSION
from app.inventory.entrypoint import task_router

app: FastAPI = FastAPI(
    title="Prueba tecnica Inventario",
    description="Se crean y actualizan los productos del inventario",
    docs_url="/v1/docs",
    version=SERVICE_VERSION,
)

app.include_router(task_router)

@app.exception_handler(exc_class_or_status_code=RequestValidationError)
async def validation_exception_handler(
    request: Request, exception: RequestValidationError
):
    return await request_validation_exception_handler(request, exception)

@app.exception_handler(IntegrityError)
async def value_error_handler(request: Request, exception: IntegrityError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "detail":[
                {
                    "type":"IntegrityError",
                    "message": "El registro esta duplicado en la base de datos"
                }
            ]
            
        }
    )