import pytest
from src.backend.clients.climatempo_client import ClimaTempoClient

def test_get_city_id():
    """Testa se a API retorna um ID válido para uma cidade"""
    city_id = ClimaTempoClient.get_city_id("São Paulo", "SP")
    assert isinstance(city_id, int), "O ID da cidade deve ser um número inteiro"

def test_get_weather():
    """Testa se a API retorna dados de clima válidos"""
    city_id = ClimaTempoClient.get_city_id("São Paulo", "SP")
    weather_data = ClimaTempoClient.get_weather(city_id)

    assert weather_data is not None, "A API deve retornar dados de clima"
    assert "data" in weather_data, "Resposta deve conter uma chave 'data'"
    assert "temperature" in weather_data["data"], "Dados devem conter temperatura"
