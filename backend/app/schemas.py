from pydantic import BaseModel
from typing import Optional

class MediaBase(BaseModel):
    title: str
    director: str
    genre: str
    platform: str
    status: str

class MediaCreate(MediaBase):
    pass

class Media(MediaBase):
    id: int

    class Config:
        orm_mode = True
class EpisodeProgressBase(BaseModel):
    media_id: int
    season: int
    episode: int
    status: str

class EpisodeProgressCreate(EpisodeProgressBase):
    pass

class EpisodeProgress(EpisodeProgressBase):
    id: int
    class Config:
        orm_mode = True

# --- Review ---
class ReviewBase(BaseModel):
    media_id: int
    rating: int
    review_text: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    class Config:
        orm_mode = True