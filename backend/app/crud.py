from sqlalchemy.orm import Session
from . import models, schemas

def get_media(db: Session):
    return db.query(models.Media).all()

def create_media(db: Session, media: schemas.MediaCreate):
    db_media = models.Media(**media.dict())
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media
