from sqlalchemy import Column, ForeignKey, Integer, String, Table
from config.db import Base


# Tabla intermedia para la relación muchos a muchos entre Singer y Song
singer_songs = Table('singer_songs', Base.metadata,
    Column('singer_id', Integer, ForeignKey('Singers.id')),
    Column('song_id', Integer, ForeignKey('Songs.id'))
)