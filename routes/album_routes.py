from fastapi import APIRouter, Depends, HTTPException,status
from config.db import  Session, get_db
from schemas.album_schema import AlbumSchema
from sqlalchemy.orm.exc import NoResultFound
from repositories.album_repository import AlbumRepository
from typing import List


album_route = APIRouter(
    tags=["Albums"]
)
##REQUERIMIENTO 2:
#music-store/api/v1/singers/{id}/ -> lista de álbumes de un artista
@album_route.get("/singers/{id}", response_model=List[AlbumSchema], status_code=status.HTTP_200_OK)
def GetAlbumByArtistId(id:int,db: Session = Depends(get_db),album_repo: AlbumRepository = Depends(AlbumRepository)) -> List[AlbumSchema]:
    return album_repo.get_albums_by_singer_id(db=db,singer_id=id)
