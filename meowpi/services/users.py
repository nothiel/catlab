from datetime import datetime
from pydantic import BaseModel


class UserSchema(BaseModel):
    full_name: str
    birth_date: datetime
    email: str
    username: str

class UserSensitiveData(UserSchema):
    hashed_password: str

class UserModifySchema(BaseModel):
    email: str | None = None
    hashed_password: str | None = None