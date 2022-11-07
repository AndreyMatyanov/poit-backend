from pydantic import parse_obj_as
from requests import Session

from app.crud.schedule_day_crud import schedule_day_crud
from app.schemas.lesson import CreateScheduleDay, ScheduleDay


def create_schedule_day(db: Session, schedule_day_create: CreateScheduleDay):
    schedule_day = schedule_day_crud.create(db=db, obj_in=schedule_day_create)
    return parse_obj_as(ScheduleDay, schedule_day)
