from typing import List
from sqlalchemy.orm import Session
from models.artist_model import ArtistModel
from schemas.artist_schema import ArtistSchema

class SingerRepository:


    # Req1: Get ALL Artists from db
    def get_all_singers(self, db: Session) -> List[ArtistSchema]:

        singers_list: List[ArtistSchema] = db.query(ArtistModel).all()

        return singers_list
    
    
    #get a singer by his id
    def get_singer_by_id(self, db: Session, singer_id: int) -> ArtistSchema:
        return db.query(ArtistModel).filter(ArtistModel.ArtistId == singer_id).first()

