from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, UUID4, Field, validator, EmailStr

from app.schemas.user import User, UserBase


class SessionBase(BaseModel):
    token: UUID4 = Field(..., alias="access_token")
    expires: datetime
    token_type: Optional[str] = "bearer"
    user_id: int

    class Config:
        allow_population_by_field_name = True,
        orm_mode = True

    @validator("token")
    def hexlify_token(cls, value):
        return value.hex


class UserTest(BaseModel):
    email: str

    class Config:
        orm_mode = True


class UserSession(SessionBase):
    id: int
    user: UserBase


class CreateUserSession(SessionBase):
    user_id: int


class UpdateUserSession(BaseModel):
    expires: datetime
