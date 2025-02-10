from fastapi import HTTPException, Depends
from src.backend.schemas.weather_schema import WeatherRequest, WeatherResponse
from src.backend.services.weather_service import WeatherService

class WeatherController:
    @staticmethod
    async def get_weather(request: WeatherRequest = Depends()) -> WeatherResponse:
        """ Busca o clima ou registra a cidade, se necessário """
        
        response = await WeatherService.get_weather(request.city_name, request.state)  # 🔹 Agora chama `WeatherService` de forma assíncrona

        if not response or "status" not in response:
            raise HTTPException(status_code=500, detail="Erro ao buscar o clima. Resposta inesperada.")

        if response["status"] == "error":
            raise HTTPException(status_code=400, detail=response["message"])

        return WeatherResponse(
            cidade=response["cidade"],
            temperatura=response["temperatura"],
            descricao=response["descricao"],
            umidade=response["umidade"],
            vento=response.get("vento", "N/A")
        )
