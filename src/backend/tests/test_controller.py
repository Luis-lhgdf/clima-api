import pytest
from src.backend.controllers.weather_controller import WeatherController

@pytest.mark.asyncio
async def test_weather_controller():
    """Testa se o controlador retorna a previsão do tempo corretamente"""
    response = await WeatherController.get_weather("São Paulo", "SP")

    assert response is not None, "O controlador deve retornar os dados de previsão do tempo"
    assert response.cidade == "São Paulo", "O nome da cidade deve estar correto"
    assert response.temperatura, "A temperatura deve estar presente"
