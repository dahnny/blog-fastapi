from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg2.extras import RealDictCursor


import psycopg2
import time

from . import models
from .routers import posts, users, auth, vote
from fastapi import FastAPI
from .database import engine



app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from inside the app folder!"}

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

models.Base.metadata.create_all(bind=engine)

        



