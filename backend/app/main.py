from fastapi import FastAPI
from . import models
from .database import engine
from .routes import media

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(media.router)
