from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/episodes", response_model=schemas.EpisodeProgress)
def add_episode(data: schemas.EpisodeProgressCreate, db: Session = Depends(get_db)):
    return crud.add_episode(db, data)

@router.get("/episodes/{media_id}", response_model=list[schemas.EpisodeProgress])
def get_episodes(media_id: int, db: Session = Depends(get_db)):
    return crud.get_episodes_for_media(db, media_id)
