from fastapi import APIRouter, Body, Depends, HTTPException,status
from config.db import Base, Session,engine,conn
from models.singer_model import Singer as SingerModel
from schemas.singer_schema import Singer as SingerSchema
from sqlalchemy.orm.exc import NoResultFound


singer = APIRouter()
#

@singer.post("/singers")
def CreateSinger(singer: SingerSchema):
    new_singer = SingerModel(FirstName=singer.FirstName, LastName=singer.LastName)
    session = Session()
    session.add(new_singer)
    session.commit()
    session.close()
    return {"message": "Singer created successfully!!"}

@singer.get("/singers/{id}")
def GetSingerById(id: int):
    try:
        session = Session()
        singer = session.query(SingerModel).get(id)
        session.close()
        if singer is None:
            raise HTTPException(status_code=404, detail="Singer not found")
        return singer
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Singer not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")