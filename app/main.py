import uvicorn
from fastapi import FastAPI, Depends
from .routers import category, product

app = FastAPI()

app.include_router(category.router)
app.include_router(product.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
