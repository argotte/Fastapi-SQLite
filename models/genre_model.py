# Project imports
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import Relationship
from config.db import Base

# Genre Model: Genre Table
class GenreModel(Base):

    __tablename__ = 'genres'

    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)
    Tracks = Relationship('TrackModel', back_populates='Genre', lazy='joined')