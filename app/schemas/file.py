from datetime import datetime

from pydantic import BaseModel

from app.schemas.base import EnumBaseUpper


class FileType(EnumBaseUpper):
    AVATAR = "AVATAR"
    PUBLICATION = "PUBLICATION"


class File(BaseModel):
    id: int
    name: str
    file_type: FileType
    size: int
    mime_type: str
    modification_time: datetime

    class Config:
        orm_mode = True


class CreateFile(BaseModel):
    name: str
    file_type: FileType
    size: int
    mime_type: str
    modification_time: datetime


class UpdateFile(CreateFile):
    pass
