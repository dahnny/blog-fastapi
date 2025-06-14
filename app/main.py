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

        
while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            dbname='postgres',
            user='postgres',
            password='jes0sluv',
            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        break
    except Exception as e:
        print("Connection to database failed")
        print(e)
        time.sleep(2)
        


