from typing import Optional
from pydantic import BaseModel


class MediaTypeSchema(BaseModel):

    MediaTypeId: int
    Name: Optional[str]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "MediaTypeId": 1,
                "Name": "CD",
            }
        }