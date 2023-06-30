from pydantic import BaseModel

class GetAlbumsBySingerIdSchema(BaseModel):
    ArtistId:int

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "Artistid":1,
                "Name":"Generic album from Justin Bieber"
            }
        }

