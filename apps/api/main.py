from fastapi import FastAPI
import models
from router import posts
from database import engine

app = FastAPI()

app.include_router(posts.router)

# Create tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
