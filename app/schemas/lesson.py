from pydantic import BaseModel

from app.schemas.base import EnumBaseUpper
from app.schemas.group import GroupBase
from app.schemas.user import UserBase, UserTeacher


class Days(EnumBaseUpper):
    MONDAY = 'MONDAY'
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class WeekType(EnumBaseUpper):
    UP = "UP"
    DOWN = "DOWN"


class Time(EnumBaseUpper):
    FIRST = "8:30"
    SECOND = "10:25"
    THIRD = "12:30"
    FOURTH = "14:20"
    FIFTH = "16:05"


class Discipline(BaseModel):
    id: int
    discipline_name: str
    count_of_hours: int
    description: str

    class Config:
        orm_mode = True


class ScheduleDay(BaseModel):
    id: int
    week_type: str
    day: str
    time: Time

    class Config:
        orm_mode = True


class CreateScheduleDay(BaseModel):
    week_type: str
    day: str
    time: Time


class UpdateScheduleDay(CreateScheduleDay):
    pass


class Lesson(BaseModel):
    id: int
    discipline_id: int
    user_teacher_id: int
    group_id: int
    schedule_day_id: int
    group: GroupBase
    subgroup: int
    cabinet: str
    user_teacher: UserTeacher
    discipline: Discipline
    schedule_day: ScheduleDay

    class Config:
        orm_mode = True


class CreateLesson(BaseModel):
    discipline_id: int
    user_teacher_id: int
    group_id: int
    schedule_day_id: int
    subgroup: int
    cabinet: str


class UpdateLesson(CreateLesson):
    pass


class CreateDiscipline(BaseModel):
    discipline_name: str
    count_of_hours: int
    description: str


class UpdateDiscipline(CreateDiscipline):
    pass
