from sqlalchemy.orm import Relationship
from config.db import Base
from sqlalchemy import Column,Integer,String,Float,ForeignKey, UniqueConstraint


# Track Model: Track Table
class TrackModel(Base):

    __tablename__ = "tracks"
    
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    Album = Relationship('AlbumModel', back_populates='Tracks', lazy='joined')
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeId'))
    MediaType = Relationship('MediaTypeModel', back_populates='Tracks', lazy='joined')
    GenreId = Column(Integer, ForeignKey('genres.GenreId'))
    Genre = Relationship('GenreModel', back_populates='Tracks', lazy='joined')
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)