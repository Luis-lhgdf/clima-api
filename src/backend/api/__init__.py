from fastapi import APIRouter
from src.backend.api.v1 import router as v1_router

api_router = APIRouter()

# ✅ Agora todas as rotas de v1 ficam dentro de `/v1`
api_router.include_router(v1_router, prefix="/v1")
