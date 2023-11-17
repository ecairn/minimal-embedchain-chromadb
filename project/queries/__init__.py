from fastapi import APIRouter
from .routes import router
from . import routes

queries_router = APIRouter()
queries_router.include_router(router)
