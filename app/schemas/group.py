from datetime import datetime

from pydantic import BaseModel

from app.schemas.base import EnumBaseUpper


class GroupName(EnumBaseUpper):
    PIR = "ПИР"
    ASOIR = "АСОИР"


class GroupBase(BaseModel):
    group_number: int
    group_name: GroupName
    count_of_subgroup: int

    class Config:
        orm_mode = True


class CreateGroup(GroupBase):
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        orm_mode = True


class UpdateGroup(CreateGroup):
    pass
