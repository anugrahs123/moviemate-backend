from fastapi import FastAPI
from . import models
from .database import engine
from .routes import media, episodes, reviews

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(media.router)
app.include_router(episodes.router)
app.include_router(reviews.router)