from pydantic import BaseModel

class CreateSongSchema(BaseModel):
    Album_ID:int
    Name:str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Album_ID": 1,
                "Name":"Baby"
            }
        }

class GetSongByIdSchema(BaseModel):
    id:int
    Album_ID:int
    Name:str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "Album_Id":1,
                "Name":"Baby"
            }
        }
     
