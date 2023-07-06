from typing import List
from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from models.singer_model import SingerModel
from models.song_model import SongModel
from schemas.singer_schema import Singer as SingerSchema, GetAllSingersSchema,CreateSingerSchema,GetSingerByIdSchema

class SingerRepository:


    # Get ALL Artists from db
    def get_all_singers(self, db: Session) -> List[GetAllSingersSchema]:

        singers_list: List[GetAllSingersSchema] = db.query(SingerModel).all()

        return singers_list
    
    def create_singer(self,db:Session,singer:CreateSingerSchema)->int:
        singer_data=SingerModel(**singer.dict())
        db.add(singer_data)
        db.commit()
        db.refresh(singer_data)
        return singer_data.id
    
    #get a singer by his id
    def get_singer_by_id(self, db: Session, singer_id: int) -> GetSingerByIdSchema:
        return db.query(SingerModel).filter(SingerModel.id == singer_id).first()

