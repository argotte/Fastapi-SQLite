# Project imports
from typing import Optional
from pydantic import BaseModel


# Genre Schema: Use for the Gender data schema
class GenreSchema(BaseModel):

    GenreId: int
    Name: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "GenreId": 1,
                "Name": "R&B"
            }
        }