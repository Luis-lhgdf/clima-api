from pydantic import BaseModel, Field
from typing import Optional

class WeatherRequest(BaseModel):
    """Validação da entrada do usuário"""
    city_name: str = Field(..., min_length=2, max_length=100, example="São Paulo")
    state: str = Field(..., min_length=2, max_length=2, example="SP")

class WeatherResponse(BaseModel):
    """Modelo de resposta da API para clima"""
    cidade: str = Field(..., example="São Paulo")
    temperatura: str = Field(..., example="25°C")
    descricao: str = Field(..., example="Parcialmente nublado")
    umidade: str = Field(..., example="60%")
    vento: Optional[str] = Field(None, example="5 km/h")
