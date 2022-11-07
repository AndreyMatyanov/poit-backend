from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, UUID4, Field, validator

from app.schemas.base import EnumBaseUpper
from app.schemas.group import GroupBase


class RoleType(EnumBaseUpper):
    USER = 'USER'
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    ADMIN = 'ADMIN'
    OWNER = 'OWNER'


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    surname: str
    second_name: str
    password: str


class UserUpdate(UserCreate):
    pass


class UserBase(BaseModel):
    id: int
    email: EmailStr
    name: str
    surname: str
    second_name: str
    is_admin: bool
    role: RoleType

    class Config:
        orm_mode = True
        validation = False


class TokenBase(BaseModel):
    token: UUID4 = Field(..., alias="access_token")
    expires: datetime
    token_type: Optional[str] = "bearer"

    class Config:
        allow_population_by_field_name = True,
        orm_mode = True

    @validator("token")
    def hexlify_token(cls, value):
        return value.hex


class User(UserBase):
    token: TokenBase = {}


class UserTeacher(UserBase):
    job_title: str
    rank: str


class UserStudent(UserBase):
    start_of_studing: datetime
    number_of_ticket: int
    group: GroupBase
    subgroup: int


class UserTeacherCreate(UserCreate):
    job_title: str
    rank: str


class UserTeacherUpdate(UserUpdate):
    pass


class UserStudentCreate(UserCreate):
    start_of_studing: datetime
    number_of_ticket: int
    group_id: int
    subgroup: int


class UserStudentUpdate(UserUpdate):
    pass
