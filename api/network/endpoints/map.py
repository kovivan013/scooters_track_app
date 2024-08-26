from fastapi import APIRouter


map_router = APIRouter()


@map_router.post("/")
async def collect_map():
    return 1