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
class GetAllSingers(BaseModel):
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

