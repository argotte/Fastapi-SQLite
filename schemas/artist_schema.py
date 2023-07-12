from typing import Optional
from pydantic import BaseModel

#Artist Schema: Use for the Artist data
class ArtistSchema(BaseModel):

    ArtistId: int
    Name: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "ArtistId": 1,
                "Name": "Michael Jackson"
            }
        }
