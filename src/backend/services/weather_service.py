from fastapi import HTTPException
from src.backend.clients.climatempo_client import ClimaTempoClient

class WeatherService:
    @staticmethod
    async def get_weather(city_name: str, state: str = "SP"):
        """Busca o ID da cidade e, depois, o clima. Se necessário, registra a cidade antes de tentar novamente."""

        city_id = await ClimaTempoClient.get_city_id(city_name, state)  # 🔹 Agora é assíncrono
        if not city_id:
            raise HTTPException(status_code=400, detail="Cidade não encontrada")

        weather_data = await ClimaTempoClient.get_weather(city_id)  # 🔹 Agora é assíncrono

        # 🔹 Se a cidade precisar ser registrada
        if weather_data is None or "error" in weather_data:
            register_response = await ClimaTempoClient.register_city(city_id)  # 🔹 Agora é assíncrono

            if not register_response["success"]:
                # 🔹 Se o erro for sobre o limite de 24 horas, retorna o tempo restante com todas as informações
                if "tempo_restante" in register_response:
                    raise HTTPException(
                        status_code=400,
                        detail={
                            "message": register_response["message"],
                            "ultima_atualizacao": register_response.get("ultima_atualizacao"),
                            "proximo_horario": register_response.get("proximo_horario"),
                            "tempo_restante": register_response["tempo_restante"]
                        }
                    )

                raise HTTPException(status_code=400, detail=f"Erro ao registrar a cidade: {register_response['message']}")

            # 🔹 Tenta buscar o clima novamente após o registro
            weather_data = await ClimaTempoClient.get_weather(city_id)  # 🔹 Agora é assíncrono

            if not weather_data:
                raise HTTPException(status_code=400, detail="Clima ainda não disponível após registro.")

        return {
            "status": "success",
            "cidade": weather_data["name"],
            "temperatura": f"{weather_data['data']['temperature']}°C",
            "descricao": weather_data["data"]["condition"],
            "umidade": f"{weather_data['data']['humidity']}%",
            "vento": f"{weather_data['data']['wind_velocity']} km/h",
        }
