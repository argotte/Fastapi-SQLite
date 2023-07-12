from sqlalchemy.orm import Relationship
from config.db import Base
from sqlalchemy import Column,Integer,String,Float,ForeignKey, UniqueConstraint


class AlbumModel(Base):

    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('artists.ArtistId'))
    Artist = Relationship('ArtistModel', back_populates='Albums', lazy='joined')
    Tracks = Relationship('TrackModel', back_populates='Album', lazy='joined')