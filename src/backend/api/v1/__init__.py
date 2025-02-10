from fastapi import APIRouter
from src.backend.api.v1.weather_routes import router as weather_router

router = APIRouter()


router.include_router(weather_router, prefix="", tags=["Previsão do Tempo - v1"])
