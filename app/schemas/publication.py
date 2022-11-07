from datetime import datetime
from typing import Optional

from fastapi_pagination import Params
from pydantic import BaseModel, Field

from app.schemas.base import OrderingType, EnumBaseUpper
from app.schemas.file import File


class PublicationType(EnumBaseUpper):
    DEFAULT = "DEFAULT"
    SCIENCE = "SCIENCE"


class PublicationBase(BaseModel):
    id: int
    title: str
    author_id: int
    publication_type: PublicationType
    description: str
    created_at: datetime
    updated_at: datetime
    file: File

    class Config:
        orm_mode = True


class Publication(BaseModel):
    title: str
    author_id: int
    publication_type: PublicationType
    description: str
    created_at: datetime
    updated_at: datetime
    file: File

    class Config:
        orm_mode = True


class CreatePublication(BaseModel):
    file_id: int
    title: str
    author_id: int
    publication_type: PublicationType
    description: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True


class UpdatePublication(CreatePublication):
    updated_at: datetime = datetime.now()


class PublicationParams(Params):
    page: int = Field(1, ge=1, description="Page number")
    size: int = Field(20, ge=1, le=100, description="Page size")
    sort: OrderingType = 'asc'
    title: Optional[str]
    author_id: Optional[int]
