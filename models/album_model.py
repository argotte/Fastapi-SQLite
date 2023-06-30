from sqlalchemy.orm import Relationship
from config.db import Base
from sqlalchemy import Column,Integer,String,Float,ForeignKey
from .MM_models import singer_albums


class AlbumModel(Base):
    __tablename__="Albums"
    id=Column(Integer,primary_key=True,autoincrement=True)
    Name=Column(String,index=True)
    #Relationship('NOMBRE DE LA CLASE',back_populates='NOMBRE DE SU ATRIBUTO')
    Songs = Relationship('SongModel',back_populates='Album')
    Singer = Relationship('SingerModel',secondary=singer_albums,back_populates='Albums')