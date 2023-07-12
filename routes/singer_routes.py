from fastapi import APIRouter, Depends, HTTPException,status
from config.db import  Session, get_db
from schemas.artist_schema import ArtistSchema
from repositories.singer_repository import SingerRepository
from typing import List


singer_route = APIRouter(
    tags=["Singers"]
)
#

##Requerimiento 1: LISTA TOTAL DE ARTISTAS
@singer_route.get("/singers/", response_model=List[ArtistSchema], status_code=status.HTTP_200_OK,summary="GET LIST OF ALL ARTISTS")
def get_singers_list(db: Session = Depends(get_db),singer_repo: SingerRepository = Depends(SingerRepository)) -> List[ArtistSchema]:
    
    return singer_repo.get_all_singers(db=db)
