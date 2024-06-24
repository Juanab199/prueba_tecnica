from fastapi import FastAPI

from app import SERVICE_VERSION

app: FastAPI = FastAPI(
    title="Máquina de decisiones prescore",
    description="Originación de creditos digitales",
    docs_url="/v1/docs",
    version=SERVICE_VERSION,
)
