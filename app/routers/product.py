from fastapi import APIRouter
from app.services.product import ProductService

router = APIRouter(
    prefix="/product",
    tags=["products"]
)


@router.get("/products/")
async def get_product():
    return [{"teste": "product1"}, {"teste": "product2"}]


@router.get("/{id}")
async def read_user(id: str):
    return {"product": id}
