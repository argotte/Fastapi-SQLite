from typing import List
from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from models.artist_model import ArtistModel
from models.track_model import TrackModel
from schemas.track_schema import TrackSchema

class SongRepository:

    
    #Get a song by his id
    def get_song_by_id(self,db:Session,song_id:int) -> TrackSchema:
        return db.query(TrackModel).filter(TrackModel.TrackId == song_id).first()
 
     #Req 3: Get all tha songs by the id of its album
    def get_song_by_album_id(self,db:Session,Album_ID:int) -> TrackSchema:
        return db.query(TrackModel).filter(TrackModel.AlbumId == Album_ID).all()
    
    #Req 4: Get song by singer Id
    def get_song_by_singer_id(self,db:Session,Singer_Id:int)-> TrackSchema:
        return db.query(TrackModel).join(AlbumModel,AlbumModel.AlbumId == TrackModel.AlbumId).join(ArtistModel,ArtistModel.ArtistId==AlbumModel.ArtistId).filter(ArtistModel.ArtistId==Singer_Id).all()