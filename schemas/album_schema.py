from pydantic import BaseModel

class GetAlbumsBySingerIdSchema(BaseModel):
    Singer_Id:int
    id:int
    Name:str

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "id":1,
                "Singer_Id":1,
                "Name":"Generic album from Justin Bieber"
            }
        }

class GetAlbumById(BaseModel):
    id:int
    Singer_Id:int
    Name:str
    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "id":1,
                "Singer_Id":1,
                "Name":"My World 2.0"
            }
        }

class CreateAlbumSchema(BaseModel):
    Singer_Id:int
    Name:str

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "Singer_Id":1,
                "Name":"My World 2.0"
            }
        }
