from sqlalchemy.orm import Relationship
from config.db import Base
from sqlalchemy import Column,Integer,String,Float,ForeignKey, UniqueConstraint


class SongModel(Base):
    __tablename__="Songs"
    id=Column(Integer,primary_key=True,autoincrement=True)
    Album_ID = Column(Integer,ForeignKey('Albums.id'))
    Name=Column(String,index=True)
    Album= Relationship('AlbumModel',back_populates='Songs')

    # Agregar restricción UNIQUE para Album_ID y Name
    __table_args__ = (UniqueConstraint('Album_ID', 'Name', name='_album_name_uc'),)
    