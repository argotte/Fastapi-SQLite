from typing import List
from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from models.song_model import SongModel
from schemas.album_schema import GetAlbumsBySingerIdSchema

class AlbumRepository:


    # Get ALL Artists from db
    def get_albums_by_artist_id(self, db: Session) -> List[GetAlbumsBySingerIdSchema]:
        album_list: List[GetAlbumsBySingerIdSchema] = db.query(AlbumModel).all()
        return album_list

