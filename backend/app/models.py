from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    genre = Column(String)
    platform = Column(String)  
    status = Column(String)    # watching, completed, wishlist
    episodes = relationship("EpisodeProgress", back_populates="media", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="media", cascade="all, delete-orphan")


class EpisodeProgress(Base):
    __tablename__ = "episode_progress"
    id = Column(Integer, primary_key=True, index=True)
    media_id = Column(Integer, ForeignKey("media.id"))
    season = Column(Integer)
    episode = Column(Integer)
    status = Column(String)  # watched/unwatched

    media = relationship("Media", back_populates="episodes")


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    media_id = Column(Integer, ForeignKey("media.id"))
    rating = Column(Integer)  # 1-5 stars
    review_text = Column(String)

    media = relationship("Media", back_populates="reviews")