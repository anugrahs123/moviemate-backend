from pydantic import BaseModel

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
