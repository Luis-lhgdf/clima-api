import asyncio
import uvicorn
from fastapi import FastAPI
from src.backend.api import api_router

app = FastAPI(
    title="API de Clima",
    version="1.0",
    description="API para buscar clima e registrar cidades na ClimaTempo",
)

# ✅ Inclui todas as versões da API automaticamente
app.include_router(api_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "API funcionando!"}


async def start():
    """Inicia o servidor FastAPI usando uvicorn de forma assíncrona."""
    config = uvicorn.Config("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(start())  # ✅ Executa o servidor de forma totalmente assíncrona
