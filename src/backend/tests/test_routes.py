import pytest
from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)

def test_get_weather():
    """Testa a rota de obtenção do clima"""
    response = client.post("/api/v1/weather/", params={"city_name": "São Paulo", "state": "SP"})

    assert response.status_code == 200, f"Esperado 200, mas retornou {response.status_code}"
    json_data = response.json()
    assert "cidade" in json_data, "Resposta deve conter a chave 'cidade'"
    assert "temperatura" in json_data, "Resposta deve conter a chave 'temperatura'"
