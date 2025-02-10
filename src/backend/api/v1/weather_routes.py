from fastapi import APIRouter, Depends
from src.backend.controllers.weather_controller import WeatherController
from src.backend.schemas.weather_schema import WeatherRequest, WeatherResponse

router = APIRouter()

@router.post("/weather/", summary="Obter ou Registrar uma Cidade", response_model=WeatherResponse)
async def get_weather(request: WeatherRequest = Depends()):
    """Se a cidade já existir, retorna o clima. Caso contrário, tenta registrá-la."""
    return await WeatherController.get_weather(request)
