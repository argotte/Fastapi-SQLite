from typing import List
from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from models.singer_model import SingerModel
from models.song_model import SongModel
from schemas.singer_schema import Singer as SingerSchema, GetAllSingersSchema

class SingerRepository:


    # Get ALL Artists from db
    def get_all_artists(self, db: Session) -> List[GetAllSingersSchema]:

        artist_list: List[GetAllSingersSchema] = db.query(SingerModel).all()

        return artist_list

