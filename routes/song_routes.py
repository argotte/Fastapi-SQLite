from fastapi import APIRouter, Depends, HTTPException,status
from config.db import  Session, get_db
from schemas.track_schema import TrackSchema
from sqlalchemy.orm.exc import NoResultFound
from repositories.singer_repository import SingerRepository
from repositories.song_repository import SongRepository
from typing import List


song_route = APIRouter(
    tags=["Songs"]
)


##Requerimiento 3:
##music-store/api/v1/albums/{id}/ -> lista de canciones del álbum de un artista
@song_route.get("/albums/{id}", response_model=List[TrackSchema], status_code=status.HTTP_200_OK,summary='GET ALL SONGS BY THE ID OF ITS ALBUM')
def GetSongsByAlbumId(id:int,db: Session = Depends(get_db),song_repo: SongRepository = Depends(SongRepository)) -> List[TrackSchema]:
    return song_repo.get_song_by_album_id(db=db,Album_ID=id)

##Requerimiento 4:
##music-store/api/v1/singer/{id}/ -> lista total de canciones de un artista
@song_route.get("/singer/{id}",response_model=List[TrackSchema],status_code=status.HTTP_200_OK,summary='GET ALL SONGS BY THE ID OF ITS ARTIST')
def get_all_songs(id:int, db:Session = Depends(get_db),song_repo:SongRepository = Depends(SongRepository)) -> List[TrackSchema]:
    return song_repo.get_song_by_singer_id(db=db,Singer_Id=id)

##Requerimiento 5:
##music-store/api/v1/song/{id}/ -> detalle de una canción por su id
@song_route.get("/song/{id}",response_model=TrackSchema,status_code=status.HTTP_200_OK,summary='GET SONG BY ID')
def get_song_by_id(id:int,db:Session=Depends(get_db),song_repo:SongRepository=Depends(SongRepository))->TrackSchema:
    return song_repo.get_song_by_id(db=db,song_id=id)