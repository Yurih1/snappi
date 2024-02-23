from fastapi import APIRouter
from app.services.category import CategoryService

router = APIRouter(
    prefix="/category",
    tags=["categories"]
)


@router.get("/categories/")
async def get_categories():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/category/{id}")
async def read_category(id: str):
    return {"category": id}
