from sqlalchemy.orm import Relationship
from config.db import Base
from sqlalchemy import Column,Integer,String
from .MM_models import singer_albums,singer_songs


class SingerModel(Base):
    __tablename__="Singers"
    id=Column(Integer,primary_key=True,autoincrement=True)
    FirstName=Column(String,index=True)
    LastName=Column(String,index=True)
    #Relationship('NOMBRE DE LA CLASE',back_populates='NOMBRE DE SU ATRIBUTO')
    Albums = Relationship('AlbumModel',secondary=singer_albums,back_populates='Singer')
    Songs = Relationship('SongModel',secondary=singer_songs,back_populates='Singer')
    