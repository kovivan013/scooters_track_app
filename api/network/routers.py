from fastapi import APIRouter
from .endpoints.debug import debug_router
from .endpoints.map import map_router


api_router = APIRouter()

api_router.include_router(
    debug_router,
    prefix="/debug",
    tags=["Debug"]
)
api_router.include_router(
    map_router,
    prefix="/map",
    tags=["Map"]
)
