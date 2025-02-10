from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Union

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

# 🔻 Modelos de erro para documentação
class APIErrorResponse(BaseModel):
    """Erro genérico da API"""
    error: bool = Field(..., example=True)
    detail: Union[str, Dict[str, str]]

class ValidationErrorDetail(BaseModel):
    """Detalhes de erro de validação"""
    loc: List[str] = Field(..., example=["query", "city_name"])
    msg: str = Field(..., example="Campo obrigatório")
    type: str = Field(..., example="value_error.missing")

class ValidationErrorResponse(BaseModel):
    """Erro de validação do FastAPI"""
    detail: List[ValidationErrorDetail]
