from sqlalchemy.orm import Relationship
from config.db import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint


# Album Model: Album Table
class ArtistModel(Base):

    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    Albums = Relationship('AlbumModel', back_populates='Artist', lazy='joined')