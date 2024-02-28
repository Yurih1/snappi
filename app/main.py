import uvicorn
from fastapi import FastAPI, Depends
from .routers import category, product, story

app = FastAPI()

app.include_router(category.router)
app.include_router(product.router)
app.include_router(story.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
