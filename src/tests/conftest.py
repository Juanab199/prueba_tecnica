import os
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture
def app() -> FastAPI:
    from app.main import app as fastapi_app

    yield fastapi_app
@pytest.fixture

def client(app) -> TestClient:
    with TestClient(app) as client:
        return client