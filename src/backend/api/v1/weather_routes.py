from fastapi import APIRouter, Depends
from src.backend.controllers.weather_controller import WeatherController
from src.backend.schemas.weather_schema import (
    WeatherRequest,
    WeatherResponse,
    APIErrorResponse,
    ValidationErrorResponse
)

router = APIRouter()

@router.post(
    "/weather/",
    summary="Obter ou Registrar uma Cidade",
    response_model=WeatherResponse,
    description="Se a cidade já existir, retorna o clima. Caso contrário, tenta registrá-la.",
    responses={
        400: {
            "description": "Erro ao buscar cidade, registrar ou obter clima",
            "model": APIErrorResponse,
            "content": {
                "application/json": {
                    "examples": {
                        "cidade_nao_encontrada": {
                            "summary": "Cidade não encontrada",
                            "value": {"error": True, "detail": "Cidade não encontrada"}
                        },
                        "erro_registro": {
                            "summary": "Erro ao registrar cidade",
                            "value": {"error": True, "detail": "Erro ao registrar a cidade: Limite atingido"}
                        },
                        "clima_indisponivel": {
                            "summary": "Clima ainda não disponível após registro",
                            "value": {"error": True, "detail": "Clima ainda não disponível após registro."}
                        },
                        "limite_registro": {
                            "summary": "Registro bloqueado por 24h",
                            "value": {
                                "error": True,
                                "detail": {
                                    "message": "Registro de cidade bloqueado pelo limite de 24 horas.",
                                    "ultima_atualizacao": "2025-02-09 22:59:00",
                                    "proximo_horario": "2025-02-10 22:59:00",
                                    "tempo_restante": "0 dias, 22 horas, 47 minutos e 11 segundos."
                                }
                            }
                        }
                    }
                }
            }
        },
        422: {
            "description": "Erro de validação do FastAPI",
            "model": ValidationErrorResponse,
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["query", "city_name"],
                                "msg": "Campo obrigatório",
                                "type": "value_error.missing",
                            }
                        ]
                    }
                }
            },
        },
    },
)
async def get_weather(request: WeatherRequest = Depends()):
    """Se a cidade já existir, retorna o clima. Caso contrário, tenta registrá-la."""
    return await WeatherController.get_weather(request)
