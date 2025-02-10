import pytest
from src.backend.services.weather_service import WeatherService

@pytest.mark.asyncio
async def test_weather_service():
    """Testa se o serviço retorna os dados corretamente"""
    response = await WeatherService.get_weather("São Paulo", "SP")

    assert response is not None, "O serviço deve retornar um dicionário"
    assert "cidade" in response, "Resposta deve conter o nome da cidade"
    assert "temperatura" in response, "Resposta deve conter a temperatura"
    assert "descricao" in response, "Resposta deve conter a descrição do clima"
