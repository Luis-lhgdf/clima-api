import aiohttp  # ✅ Usa aiohttp para requisições assíncronas
from datetime import datetime, timedelta
import pytz
import re
from src.backend.core.config import settings


class ClimaTempoClient:
    BASE_URL = "http://apiadvisor.climatempo.com.br/api/v1"
    TOKEN = settings.CLIMATEMPO_API_KEY

    @staticmethod
    async def get_city_id(city_name: str, state: str, country: str = "BR"):
        """ Retorna o ID da cidade na API ClimaTempo """

        url = f"{ClimaTempoClient.BASE_URL}/locale/city?name={city_name}&state={state}&country={country}&token={ClimaTempoClient.TOKEN}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    city_data = await response.json()
                    if city_data:
                        return city_data[0]["id"]  # Retorna o primeiro resultado

        return None

    @staticmethod
    async def get_weather(city_id: int):
        """ Busca as informações do clima de uma cidade pelo ID """
        
        url = f"{ClimaTempoClient.BASE_URL}/weather/locale/{city_id}/current?token={ClimaTempoClient.TOKEN}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()

                if response.status == 400:
                    error_data = await response.json()
                    if "Access forbidden" in error_data.get("detail", ""):
                        return {"error": "register_required", "message": f"Registro necessário para a cidade ID {city_id}"}

        return None

    @staticmethod
    def calcular_tempo_restante(mensagem_erro):
        """ Calcula quanto tempo falta para poder registrar a cidade novamente """

        # Extraindo a data do erro da mensagem com regex
        match = re.search(r"\((\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) ([^\)]+)\)", mensagem_erro)
        if not match:
            return {"success": False, "message": "Formato de mensagem inválido."}

        data_erro_str, fuso_horario_str = match.groups()

        # Pegando apenas o nome do fuso horário
        tz_name = fuso_horario_str.split(" ")[0]
        tz = pytz.timezone(tz_name)

        try:
            # Convertendo a string para um objeto datetime com fuso horário
            data_erro = tz.localize(datetime.strptime(data_erro_str, "%Y-%m-%d %H:%M:%S"))
        except ValueError:
            return {"success": False, "message": "Formato de data inválido."}

        # Definindo o tempo limite de 24 horas
        tempo_limite = data_erro + timedelta(hours=24)

        # Obtendo a data e hora atual no mesmo fuso horário
        agora = datetime.now(tz)

        # Calculando o tempo restante
        tempo_restante = tempo_limite - agora

        # Se o tempo já expirou, pode registrar agora
        if tempo_restante.total_seconds() < 0:
            return {
                "success": True,
                "message": "O tempo já expirou, você pode registrar agora.",
                "ultima_atualizacao": data_erro.strftime('%Y-%m-%d %H:%M:%S'),
                "proximo_horario": tempo_limite.strftime('%Y-%m-%d %H:%M:%S')
            }

        # Convertendo para horas, minutos e segundos
        horas = tempo_restante.seconds // 3600
        minutos = (tempo_restante.seconds % 3600) // 60
        segundos = tempo_restante.seconds % 60

        return {
            "success": False,
            "message": "Registro de cidade bloqueado pelo limite de 24 horas.",
            "ultima_atualizacao": data_erro.strftime('%Y-%m-%d %H:%M:%S'),
            "proximo_horario": tempo_limite.strftime('%Y-%m-%d %H:%M:%S'),
            "tempo_restante": f"{tempo_restante.days} dias, {horas} horas, {minutos} minutos e {segundos} segundos."
        }

    @staticmethod
    async def register_city(city_id: int):
        """ Registra a cidade no plano gratuito da ClimaTempo (limite de 1 cidade a cada 24h) """

        url = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/{ClimaTempoClient.TOKEN}/locales"
        
        async with aiohttp.ClientSession() as session:
            async with session.put(url, data={"localeId[]": city_id}) as response:
                if response.status == 200:
                    return {"success": True, "message": "Cidade registrada com sucesso!"}

                if response.status == 400:
                    error_message = (await response.json()).get("detail", "Erro desconhecido")

                    # Verifica se a resposta contém a restrição de tempo
                    if "Your free plan only allows to update cities after 24 hours" in error_message:
                        return ClimaTempoClient.calcular_tempo_restante(error_message)

        return {"success": False, "message": "Erro ao registrar cidade"}
