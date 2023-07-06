from fastapi import APIRouter, Body, Depends, HTTPException,status
from config.db import Base, Session,engine,conn, get_db
from models.singer_model import SingerModel
from schemas.singer_schema import Singer as SingerSchema,GetAllSingersSchema
from schemas.album_schema import GetAlbumsBySingerIdSchema,CreateAlbumSchema,GetAlbumById
from sqlalchemy.orm.exc import NoResultFound
from repositories.album_repository import AlbumRepository
from typing import List


album_route = APIRouter(
    tags=["Albums"]
)
##REQUERIMIENTO 2:
#music-store/api/v1/singers/{id}/ -> lista de álbumes de un artista
@album_route.get("/singers/{id}", response_model=List[GetAlbumsBySingerIdSchema], status_code=status.HTTP_200_OK)
def GetAlbumByArtistId(id:int,db: Session = Depends(get_db),album_repo: AlbumRepository = Depends(AlbumRepository)) -> List[GetAlbumsBySingerIdSchema]:
    return album_repo.get_albums_by_singer_id(db=db,singer_id=id)

##Crear Album
@album_route.post("/createalbum", response_model=GetAlbumById, status_code=status.HTTP_201_CREATED)
def create_album(album: CreateAlbumSchema, db: Session = Depends(get_db), album_repo: AlbumRepository = Depends(AlbumRepository)) -> GetAlbumsBySingerIdSchema:
    album_id = album_repo.create_album(db=db, album=album)
    created_album = album_repo.get_album_by_id(db=db, album_id=album_id)
    return created_album