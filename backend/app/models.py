from sqlalchemy import Column, Integer, String, Enum
from .database import Base

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    genre = Column(String)
    platform = Column(String)  
    status = Column(String)    # watching, completed, wishlist
