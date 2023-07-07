from fastapi import APIRouter, Body, Depends, HTTPException,status
from config.db import Base, Session,engine,conn, get_db
from models.singer_model import SingerModel
from schemas.singer_schema import Singer as SingerSchema,GetAllSingersSchema,CreateSingerSchema,GetSingerByIdSchema
from schemas.song_schema import CreateSongSchema,GetSongByIdSchema
from sqlalchemy.orm.exc import NoResultFound
from repositories.singer_repository import SingerRepository
from repositories.song_repository import SongRepository
from typing import List


song_route = APIRouter(
    tags=["Songs"]
)

@song_route.post("/createsong",response_model=GetSongByIdSchema,status_code=status.HTTP_201_CREATED)
def create_song(song:CreateSongSchema,db:Session=Depends(get_db),song_repo:SongRepository=Depends(SongRepository))-> GetSongByIdSchema:
    song_id=song_repo.create_song(db=db,song=song)
    created_song=song_repo.get_song_by_id(db=db,song_id=song_id)
    return created_song

##Requerimiento 3:
##music-store/api/v1/albums/{id}/ -> lista de canciones del álbum de un artista
@song_route.get("/albums/{id}", response_model=List[GetSongByIdSchema], status_code=status.HTTP_200_OK)
def GetAlbumByArtistId(id:int,db: Session = Depends(get_db),song_repo: SongRepository = Depends(SongRepository)) -> List[GetSongByIdSchema]:
    return song_repo.get_song_by_album_id(db=db,Album_ID=id)

##Requerimiento 4:
##music-store/api/v1/singer/{id}/ -> lista total de canciones de un artista
@song_route.get("/singer/{id}",response_model=List[GetSongByIdSchema],status_code=status.HTTP_200_OK)
def get_all_songs(id:int, db:Session = Depends(get_db),song_repo:SongRepository = Depends(SongRepository)) -> List[GetSongByIdSchema]:
    return song_repo.get_song_by_singer_id(db=db,Singer_Id=id)

@song_route.get("/song/{id}",response_model=GetSongByIdSchema,status_code=status.HTTP_200_OK)
def get_song_by_id(id:int,db:Session=Depends(get_db),song_repo:SongRepository=Depends(SongRepository))->GetSongByIdSchema:
    return song_repo.get_song_by_id(db=db,song_id=id)