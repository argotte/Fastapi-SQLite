from sqlalchemy.orm import Relationship
from config.db import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint
from .MM_models import singer_songs


class SingerModel(Base):
    __tablename__ = "Singers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, index=True)
    LastName = Column(String, index=True)
    Albums = Relationship('AlbumModel', back_populates='Singer')
    Songs = Relationship('SongModel', secondary=singer_songs, back_populates='Singer')

    # Add a unique constraint on the combination of FirstName and LastName columns
    __table_args__ = (UniqueConstraint('FirstName', 'LastName', name='_first_last_uc'),)