from sqlalchemy.orm import Relationship
from config.db import Base
from sqlalchemy import Column,Integer,String,Float,ForeignKey
from .MM_models import singer_songs


class SongModel(Base):
    __tablename__="Songs"
    id=Column(Integer,primary_key=True,autoincrement=True)
    Album_ID = Column(Integer,ForeignKey('Albums.id'))
    Name=Column(String,index=True)
    #Relationship('NOMBRE DE LA CLASE',back_populates='NOMBRE DE SU ATRIBUTO')
    Album= Relationship('AlbumModel',back_populates='Songs')
    Singer = Relationship('SingerModel',secondary=singer_songs,back_populates='Songs')
    