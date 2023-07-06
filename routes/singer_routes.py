from fastapi import APIRouter, Body, Depends, HTTPException,status
from config.db import Base, Session,engine,conn, get_db
from models.singer_model import SingerModel
from schemas.singer_schema import Singer as SingerSchema,GetAllSingersSchema,CreateSingerSchema,GetSingerByIdSchema
from sqlalchemy.orm.exc import NoResultFound
from repositories.singer_repository import SingerRepository
from typing import List


singer_route = APIRouter(
    tags=["Singers"]
)
#

#@singer_route.post("/singers")
#def CreateSinger(singer: SingerSchema):
#    new_singer = SingerModel(FirstName=singer.FirstName, LastName=singer.LastName)
#    session = Session()
#    session.add(new_singer)
#    session.commit()
#    session.close()
#    return {"message": "Singer created successfully!!"}

@singer_route.post("/createsinger",response_model=GetSingerByIdSchema,status_code=status.HTTP_201_CREATED)
def create_singer(singer:CreateSingerSchema,db:Session=Depends(get_db),singer_repo:SingerRepository=Depends(SingerRepository))-> GetSingerByIdSchema:
    singer_id=singer_repo.create_singer(db=db,singer=singer)
    created_singer=singer_repo.get_singer_by_id(db=db,singer_id=singer_id)
    return created_singer



##Requerimiento 1: LISTA TOTAL DE ARTISTAS
@singer_route.get("/singers/", response_model=List[GetAllSingersSchema], status_code=status.HTTP_200_OK)
def get_singers_list(db: Session = Depends(get_db),singer_repo: SingerRepository = Depends(SingerRepository)) -> List[GetAllSingersSchema]:
    
    return singer_repo.get_all_singers(db=db)

#@singer_route.get("/singers/{id}")
#def GetSingerById(id: int):
#    try:
#        session = Session()
#        singer = session.query(SingerModel).get(id)
#        session.close()
#        if singer is None:
##            raise HTTPException(status_code=404, detail="Singer not found")
#        return singer
#    except NoResultFound:
#        raise HTTPException(status_code=404, detail="Singer not found")
#    except Exception as e:
#        raise HTTPException(status_code=500, detail="Internal server error")