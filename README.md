# 📌 **Estrutura Completa do Projeto: API do Clima com FastAPI, Testes e ENV para Tokens**

Este projeto consiste em uma **API de previsão do tempo**, conectada a um serviço externo de clima, estruturada seguindo **Clean Architecture**. Também inclui **testes automatizados** e **uso de variáveis de ambiente (`.env`) para armazenar tokens de API**.

---

# 📂 **1️⃣ Estrutura Completa do Projeto**

````
📁 src
│── 📁 backend
│   ├── 📁 api               # Define os endpoints
│   │   ├── 📁 v1
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 weather_routes.py  # Rota principal
│   │   ├── 📄 __init__.py
│   ├── 📁 controllers       # Controla a lógica antes do Service
│   │   ├── 📄 weather_controller.py
│   ├── 📁 services          # Processa a lógica de negócio
│   │   ├── 📄 weather_service.py
│   ├── 📁 clients           # Comunicação com a API externa (ClimaTempo)
│   │   ├── 📄 climatempo_client.py
│   ├── 📁 schemas           # Validação com Pydantic
│   │   ├── 📄 weather_schema.py
│   ├── 📁 core              # Configurações globais
│   │   ├── 📄 config.py      # Carrega variáveis do .env
│   ├── 📁 tests             # Testes unitários e integração
│   │   ├── 📄 test_weather_service.py
│   │   ├── 📄 test_weather_controller.py
│   ├── 📄 main.py           # Ponto de entrada do FastAPI
│── 📄 .env                  # Armazena token da API do ClimaTempo
│── 📄 requirements.txt       # Dependências
│── 📄 README.md              # Documentação


---

# 🚀 **2️⃣ Como Cada Arquivo Se Conecta**

A API segue **Clean Architecture**, separando responsabilidades de forma clara.

| **Camada**         | **Responsabilidade**                                    | **Exemplo**               |
| ------------------ | ------------------------------------------------------- | ------------------------- |
| **`routes/`**      | Define os endpoints da API (`GET /weather/{city_name}`) | `weather_routes.py`       |
| **`controllers/`** | Valida a entrada antes de chamar o Service              | `weather_controller.py`   |
| **`services/`**    | Processa a lógica de negócio e chama o Client           | `weather_service.py`      |
| **`clients/`**     | Faz a requisição para a API de clima externa            | `openweather_client.py`   |
| **`schemas/`**     | Define modelos de entrada e saída com validação         | `weather_schema.py`       |
| **`core/`**        | Carrega configurações e tokens de `.env`                | `config.py`               |
| **`tests/`**       | Contém testes automatizados                             | `test_weather_service.py` |

---

# 🌍 **3️⃣ Conectando a API ao Serviço de Clima**

### 📁 **backend/clients/openweather_client.py**

```python
import requests
import os
from app.backend.core.config import settings

class OpenWeatherClient:
    @staticmethod
    def get_weather(city_name: str):
        """
        Faz a requisição para a API OpenWeather e retorna os dados.
        """
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.OPENWEATHER_API_KEY}&units=metric&lang=pt"
        response = requests.get(url)

        if response.status_code != 200:
            return None

        return response.json()
````

✅ **Puxa o token da API diretamente do `.env` e faz a requisição**.

---

# 🏗 **4️⃣ Configuração do `.env` para Token da API**

Crie um arquivo **`.env`** na raiz do projeto:

```
OPENWEATHER_API_KEY=SEU_TOKEN_AQUI
```

### 📁 **backend/core/config.py**

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENWEATHER_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
```

✅ **Agora podemos acessar `settings.OPENWEATHER_API_KEY` em qualquer parte do código!** 🚀

---

# 📡 **5️⃣ Criando os Endpoints da API**

📁 **backend/api/v1/weather_routes.py**

```python
from fastapi import APIRouter
from app.backend.controllers.weather_controller import WeatherController

router = APIRouter()

router.add_api_route("/{city_name}", WeatherController.get_weather, methods=["GET"], summary="Obter previsão do tempo")
```

✅ **Aqui só registramos a rota e deixamos o Controller cuidar do resto**.

---

📁 **backend/controllers/weather_controller.py**

```python
from fastapi import HTTPException, Depends
from app.backend.schemas.weather_schema import WeatherRequest, WeatherResponse
from app.backend.services.weather_service import WeatherService

class WeatherController:
    @staticmethod
    def get_weather(request: WeatherRequest = Depends()) -> WeatherResponse:
        """
        Recebe os dados validados pelo Schema e chama o serviço para buscar previsão do tempo.
        """
        weather = WeatherService.get_weather_data(request.city_name)

        if not weather:
            raise HTTPException(status_code=404, detail="Cidade não encontrada")

        return weather
```

✅ **Aqui validamos a entrada antes de chamar o `Service`**.

---

# 🛠 **6️⃣ Criando os Testes**

📁 **tests/unit/test_weather_service.py**

```python
from app.backend.services.weather_service import WeatherService

def test_get_weather_data():
    result = WeatherService.get_weather_data("São Paulo")
    assert result is not None
    assert "cidade" in result
    assert "temperatura" in result
```

✅ **Testa a lógica do `Service` para garantir que ele retorna os dados corretamente**.

---

📁 **tests/integration/test_weather_routes.py**

```python
from fastapi.testclient import TestClient
from app.backend.main import app

client = TestClient(app)

def test_get_weather():
    response = client.get("/api/v1/weather/Sao Paulo")
    assert response.status_code == 200
    assert "cidade" in response.json()
```

✅ **Testa se o endpoint retorna os dados corretamente**.

---

# 🚀 **7️⃣ Rodando a API e Testes**

### **Rodar a API**

```sh
uvicorn app.backend.main:app --reload
```

🔹 **Acesse a API em:** `http://localhost:8000/docs`

---

### **Rodar os Testes**

```sh
pytest tests/
```

✅ **Isso executará todos os testes unitários e de integração**.

---

# ✅ **Resumo Final**

✔ **Projeto bem estruturado seguindo Clean Architecture**.  
✔ **Conectado à API do OpenWeather** usando variáveis de ambiente.  
✔ **Testes unitários e de integração para garantir qualidade**.  
✔ **`.env` protege o token da API, sem expor no código**.
