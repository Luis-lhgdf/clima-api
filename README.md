### **📌 PROJETO COMPLETO: API de Previsão do Tempo com Frontend**

✅ **Objetivo:** Criar uma **API de previsão do tempo** que consulta a temperatura de qualquer cidade do mundo e exibe os dados em uma interface visual.  
✅ **O que você vai treinar?**

- **Backend**: FastAPI, consumo de API externa, separação em camadas (`View → Controller → Service → Client`).
- **Frontend**: HTML, Bootstrap, JavaScript para consumir a API.

---

## **📌 Como vai funcionar?**

### **1️⃣ Backend (FastAPI)**

- Criar uma **API** que recebe uma cidade e retorna a previsão do tempo.
- A API chama a **OpenWeather API** e **filtra os dados** antes de devolver.
- Exemplo de chamada:
  ```
  GET /previsao-tempo?cidade=São Paulo
  ```
- Exemplo de resposta:
  ```json
  {
    "cidade": "São Paulo",
    "temperatura": "25°C",
    "descricao": "Parcialmente nublado",
    "umidade": "60%"
  }
  ```

### **2️⃣ Frontend (Bootstrap + JavaScript)**

- Criar uma **interface moderna** onde o usuário digita o nome da cidade e vê a previsão.
- O botão **"Buscar"** chama a API do backend e exibe os dados na tela.
- Interface inspirada em aplicativos de clima.

---

## **📌 Estrutura do Projeto**

📁 O projeto será dividido em **backend** e **frontend**:

```
/src
│── /backend
│   │── main.py          # Inicializa a API FastAPI
│   │── /models         # Modelos de dados (Pydantic)
│   │   │── weather.py  # Modelo para validar resposta
│   │── /controllers    # Controladores da API
│   │   │── weather_controller.py
│   │── /services       # Processamento de regras de negócio
│   │   │── weather_service.py
│   │── /clients        # Comunicação com a API externa (OpenWeather)
│   │   │── weather_client.py
│   │── /env            # Configurações da API (chave da OpenWeather)
│   │── requirements.txt # Dependências do projeto
│
│── /frontend
│   │── index.html       # Página principal
│   │── static/style.css # Estilos (Bootstrap + customizações)
│   │── static/script.js # JavaScript para consumir API
│
│── README.md           # Documentação do projeto
```

---

## **📌 Fluxo Completo do Projeto**

```
Usuário digita a cidade no site → Frontend chama a API Backend →
Backend consulta OpenWeather → Filtra os dados → Retorna resposta JSON →
Frontend exibe os dados formatados na tela
```

---

## **📌 Requisitos do Projeto**

1️⃣ **Backend**

- Criar a API **`/previsao-tempo`** usando **FastAPI**.
- Consultar a **OpenWeather API** para obter os dados.
- **Filtrar** os dados antes de enviar a resposta.

2️⃣ **Frontend**

- Criar um **campo de busca** onde o usuário insere o nome da cidade.
- Criar um **botão de busca** que chama o backend.
- Exibir os dados do clima em **uma interface moderna**.

---

## **📌 Exemplo de Uso**

### **1️⃣ Usuário busca a cidade no frontend**

🔽 **Entrada:**

- O usuário digita **"São Paulo"** no site e clica em **Buscar**.

🔽 **A API chama a OpenWeather:**

```
GET /previsao-tempo?cidade=São Paulo
```

🔽 **Resposta do backend (dados filtrados):**

```json
{
  "cidade": "São Paulo",
  "temperatura": "25°C",
  "descricao": "Parcialmente nublado",
  "umidade": "60%"
}
```

🔽 **Frontend exibe os dados formatados**

- **Cidade:** São Paulo 🌍
- **Temperatura:** 25°C 🌡️
- **Clima:** Parcialmente nublado ☁️
- **Umidade:** 60% 💧

---

## **📌 Como funciona a OpenWeather API?**

Você precisa **criar uma conta grátis** na OpenWeather para obter uma **chave de API (`API_KEY`)**.

📌 **URL da API:**

```
https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt
```

- `{CIDADE}` → Nome da cidade digitada pelo usuário.
- `{API_KEY}` → Chave de acesso à API (grátis).
- **`units=metric`** → Retorna a temperatura em **graus Celsius**.
- **`lang=pt`** → Retorna a descrição do clima em **português**.

---

## **📌 Próximos Passos**

Agora que temos o **enunciado completo**, vamos para a **implementação**! 🚀

📌 **O que vamos fazer primeiro?**  
✅ Criar a **estrutura do projeto** com `backend/` e `frontend/`.

Me avise quando quiser começar que já preparo o primeiro código! 🚀🎯
