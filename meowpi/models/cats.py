from pydantic import BaseModel
from datetime import datetime


class CatSchema(BaseModel):
    cat_name: str
    cat_birth_date: datetime
    cat_vaccined: bool
    cat_castrated: bool
    cat_photos: list

class CatsSchema(BaseModel):
    cats: list[CatSchema]

class CatModifySchema(BaseModel):
    cat_vaccined: bool | None = None
    cat_castrated: bool | None = None 
    cat_photos: list | None = None