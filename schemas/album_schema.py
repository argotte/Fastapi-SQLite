from pydantic import BaseModel

class GetAlbumsBySingerIdSchema(BaseModel):
    SingerId:int

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "Singer_Id":1,
                "Name":"Generic album from Justin Bieber"
            }
        }

class CreateAlbumSchema(BaseModel):
    Singer_Id:int
    Name:str

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "Singer_Id":3,
                "Name":"Random Access Memories"
            }
        }
