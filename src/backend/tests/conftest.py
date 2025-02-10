import pytest
from fastapi.testclient import TestClient
from src.backend.main import app

@pytest.fixture(scope="module")
def client():
    """Fixture para o cliente de testes do FastAPI"""
    return TestClient(app)
