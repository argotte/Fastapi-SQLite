from typing import List
from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from models.song_model import SongModel
from schemas.album_schema import GetAlbumsBySingerIdSchema,CreateAlbumSchema,GetAlbumById

class AlbumRepository:


    # Get an album by the id of the singer
    def get_albums_by_singer_id(self, db: Session,singer_id:int) -> List[GetAlbumsBySingerIdSchema]:
        return db.query(AlbumModel).filter(AlbumModel.Singer_Id == singer_id).all()
    
    ##Create an album
    def create_album(self, db: Session, album: CreateAlbumSchema) -> int:
        album_data = AlbumModel(**album.dict())
        db.add(album_data)
        db.commit()
        db.refresh(album_data)
        return album_data.id

    #get an album by his id
    def get_album_by_id(self, db: Session, album_id: int) -> GetAlbumById:
        return db.query(AlbumModel).filter(AlbumModel.id == album_id).first()