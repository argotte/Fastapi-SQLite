from typing import List
from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from models.singer_model import SingerModel
from models.song_model import SongModel
from schemas.song_schema import CreateSongSchema,GetSongByIdSchema

class SongRepository:

    def create_song(self,db:Session,song:CreateSongSchema)->int:
        song_data=SongModel(**song.dict())
        db.add(song_data)
        db.commit()
        db.refresh(song_data)
        return song_data.id
    
    #Get a song by his id
    def get_song_by_id(self,db:Session,song_id:int) -> GetSongByIdSchema:
        return db.query(SongModel).filter(SongModel.id == song_id).first()
 
     #Get all tha songs by the id of its album
    def get_song_by_album_id(self,db:Session,Album_ID:int) -> GetSongByIdSchema:
        return db.query(SongModel).filter(SongModel.Album_ID == Album_ID).all()
    
    def get_song_by_singer_id(self,db:Session,Singer_Id:int)-> GetSongByIdSchema:
        return db.query(SongModel).join(AlbumModel,AlbumModel.id == SongModel.Album_ID).join(SingerModel,SingerModel.id==AlbumModel.Singer_Id).filter(SingerModel.id==Singer_Id).all()