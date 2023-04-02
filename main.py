from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from database import models
from database.database import engine
from routers import post

app = FastAPI()
app.include_router(post.router)

models.Base.metadata.create_all(engine)

origins = ['*']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=['*'],
    allow_headers=['*']
)