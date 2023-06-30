from fastapi import APIRouter, Body, Depends, HTTPException,status
from config.db import Base, Session,engine,conn, get_db
from models.singer_model import SingerModel
from schemas.singer_schema import Singer as SingerSchema,GetAllSingersSchema
from schemas.album_schema import GetAlbumsBySingerIdSchema 
from sqlalchemy.orm.exc import NoResultFound
from repositories.album_repository import AlbumRepository
from typing import List


album_route = APIRouter(
    tags=["Albums"]
)

@album_route.get("/singers/{id}", response_model=List[GetAlbumsBySingerIdSchema], status_code=status.HTTP_200_OK)
def GetAlbumByArtistId(db: Session = Depends(get_db),album_repo: AlbumRepository = Depends(AlbumRepository)) -> List[GetAlbumsBySingerIdSchema]:
    return album_repo.get_albums_by_artist_id(db=db)
