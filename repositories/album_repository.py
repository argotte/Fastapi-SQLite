from typing import List
from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from schemas.album_schema import AlbumSchema
class AlbumRepository:


    # Req2: Get an album by the id of the singer
    def get_albums_by_singer_id(self, db: Session,singer_id:int) -> List[AlbumSchema]:
        return db.query(AlbumModel).filter(AlbumModel.ArtistId == singer_id).all()
    

    #get an album by his id
    def get_album_by_id(self, db: Session, album_id: int) -> AlbumSchema:
        return db.query(AlbumModel).filter(AlbumModel.AlbumId == album_id).first()