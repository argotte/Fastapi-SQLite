from sqlalchemy.orm import Relationship
from config.db import Base
from sqlalchemy import Column,Integer,String,Float,ForeignKey


class AlbumModel(Base):
    __tablename__="Albums"
    id=Column(Integer,primary_key=True,autoincrement=True)
    Singer_Id = Column(Integer,ForeignKey('Singers.id'))
    Name=Column(String,index=True)
    #Relationship('NOMBRE DE LA CLASE',back_populates='NOMBRE DE SU ATRIBUTO')
    Songs = Relationship('SongModel',back_populates='Album')
    Singer = Relationship('SingerModel',back_populates='Albums')