# Project imports
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import Relationship
from config.db import Base


# Media Type Model: Media Type Table
class MediaTypeModel(Base):

    __tablename__ = 'media_types'

    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String)
    Tracks = Relationship('TrackModel', back_populates='MediaType', lazy='joined')