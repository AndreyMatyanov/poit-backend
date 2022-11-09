from datetime import datetime
from typing import List

from pydantic import BaseModel


class StageCourseProjectBase(BaseModel):
    id: int
    course_project_id: int
    title: str
    description: str
    is_done: bool
    deadline_date: datetime

    class Config:
        orm_mode = True


class CreateCourseProject(BaseModel):
    discipline_id: int
    user_student_id: int
    percent_of_completion: float = 0


class CreateCourseProjectRequest(BaseModel):
    create_course_prj_db: CreateCourseProject
    user_teacher_id: int
    topic_approval_date: datetime
    topic_confirmation_date: datetime
    project_completion_date: datetime
    admission_project_protection_date: datetime
    graduation_date: datetime


class CreateCourseProjectForGroupRequest(BaseModel):
    discipline_id: int
    group_id: int
    user_teacher_id: int
    topic_approval_date: datetime
    topic_confirmation_date: datetime
    project_completion_date: datetime
    admission_project_protection_date: datetime
    graduation_date: datetime


class UpdateCourseProject(CreateCourseProject):
    pass


class CreateStageCourseProject(BaseModel):
    course_project_id: int
    title: str
    description: str
    is_done: bool
    deadline_date: datetime


class UpdateStageCourseProject(CreateStageCourseProject):
    pass


class CourseProjectUserTeacherBase(BaseModel):
    id: int
    user_teacher_id: int
    course_project_id: int


class CourseProjectUserTeacher(BaseModel):
    user_teacher_id: int
    course_project_id: int


class CreateCourseProjectUserTeacher(CourseProjectUserTeacher):
    pass


class UpdateCourseProjectUserTeacher(CreateCourseProjectUserTeacher):
    pass


class CourseProjectBase(BaseModel):
    id: int
    discipline_id: int
    user_student_id: int
    percent_of_completion: float
    stages: List[StageCourseProjectBase]

    class Config:
        orm_mode = True
