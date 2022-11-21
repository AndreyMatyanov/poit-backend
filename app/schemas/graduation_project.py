from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.schemas.base import EnumBaseUpper


class PatternOfEducation(EnumBaseUpper):
    BEL = "BEL"
    RU = "RU"


class StageGraduationProjectBase(BaseModel):
    id: int
    graduation_project_id: int
    title: str
    description: str
    is_done: bool
    deadline_date: datetime

    class Config:
        orm_mode = True


class CreateStageGraduationProject(BaseModel):
    graduation_project_id: int
    title: str
    description: str
    is_done: bool
    deadline_date: datetime


class UpdateStageGraduationProject(CreateStageGraduationProject):
    pass


class CreateGraduationProject(BaseModel):
    user_student_id: int
    percent_of_completion: float = 0
    pattern_of_education: PatternOfEducation
    theme: str = "Не назначена"


class UpdateGraduationProject(CreateGraduationProject):
    pass


class GraduationProjectBase(BaseModel):
    id: int
    user_student_id: int
    percent_of_completion: float
    theme: str
    pattern_of_education: PatternOfEducation
    stages: List[StageGraduationProjectBase]

    class Config:
        orm_mode = True


class GraduationProjectBaseWithoutStage(BaseModel):
    id: int
    user_student_id: int
    percent_of_completion: float
    theme: str
    pattern_of_education: PatternOfEducation

    class Config:
        orm_mode = True


class CreateGraduationProjectRequest(BaseModel):
    create_prj_db: CreateGraduationProject
    user_teacher_id: int
    topic_approval_date: datetime
    topic_confirmation_date: datetime
    project_completion_date: datetime
    admission_project_protection_date: datetime
    graduation_date: datetime


class CreateGraduationProjectForGroupRequest(BaseModel):
    group_id: int
    user_teacher_id: int
    pattern_of_education: PatternOfEducation
    topic_approval_date: datetime
    topic_confirmation_date: datetime
    project_completion_date: datetime
    admission_project_protection_date: datetime
    graduation_date: datetime


class GraduationProjectUserTeacher(BaseModel):
    user_teacher_id: int
    graduation_project_id: int


class CreateGraduationProjectUserTeacher(GraduationProjectUserTeacher):
    pass


class UpdateGraduationProjectUserTeacher(CreateGraduationProjectUserTeacher):
    pass
