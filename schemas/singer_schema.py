from pydantic import BaseModel

class Singer(BaseModel):
    FirstName:str
    LastName:str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "FirstName": "Michael",
                "Name": "Jackson"
            }
        }
class GetAllSingersSchema(BaseModel):
    id:int
    FirstName:str
    LastName:str

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "id":1,
                "FirstName":"JB",
                "LastName":"Bieber"
            }
        }

class CreateSingerSchema(BaseModel):
    FirstName:str
    LastName:str
    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "FirstName":"Justin",
                "LastName":"Bieber"
            }
        } 

class GetSingerByIdSchema(BaseModel):
    id:int
    FirstName:str
    LastName:str

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "id":1,
                "FirstName":"Justin",
                "LastName":"Bieber"
            }
        }