from typing import Optional

from pydantic import BaseModel

from app.schemas.base import EnumBaseUpper


class StatusOfRequest(EnumBaseUpper):
    WAITING = "WAITING"
    ACCEPTED = "ACCEPTED"
    CANCELED = "CANCELED"


class GraduationRequestBase(BaseModel):
    id: int
    user_student_id: int
    user_teacher_id: int
    theme: str
    description: str
    status: StatusOfRequest

    class Config:
        orm_mode = True


class CreateGraduationRequest(BaseModel):
    user_student_id: int
    user_teacher_id: int
    theme: str
    description: str
    status: Optional[StatusOfRequest] = StatusOfRequest.WAITING


class UpdateGraduationRequest(CreateGraduationRequest):
    pass
