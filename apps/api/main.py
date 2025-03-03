from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from router import posts
from database import engine
from logger import logger
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

logger.info("Starting server")

app.include_router(posts.router)

# Create tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}
