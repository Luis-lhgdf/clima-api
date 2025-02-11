import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.backend.api import api_router

app = FastAPI(
    title="API de Clima",
    version="1.0",
    description="API para buscar clima e registrar cidades na ClimaTempo",
)

# Configuração de CORS para permitir requisições do frontend hospedado no Netlify
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui todas as versões da API automaticamente
app.include_router(api_router, prefix="/api")


@app.get("/")
async def root():
    """Testa se a API está funcionando corretamente."""
    return {"message": "API funcionando!"}


@app.get("/healthz")
async def health_check():
    """Endpoint para verificar se a API está online (para monitoramento)."""
    return {"status": "ok"}


async def start():
    """Inicia o servidor FastAPI usando uvicorn de forma assíncrona."""
    config = uvicorn.Config("src.backend.main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(start())  # ✅ Executa o servidor de forma totalmente assíncrona
