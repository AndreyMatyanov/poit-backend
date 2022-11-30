from pydantic import BaseModel

from app.schemas.user import UserTeacher


class CountOfTeacherProjectBase(BaseModel):
    id: int
    user_teacher_id: int
    max_count: int
    user: UserTeacher

    class Config:
        orm_mode = True


class CreateCountOfTeacherProject(BaseModel):
    user_teacher_id: int
    max_count: int


class UpdateCountOfTeacherProject(CreateCountOfTeacherProject):
    pass
