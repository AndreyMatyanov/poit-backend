from app.crud.base import CRUDBase
from app.models.schedule_day import ScheduleDay as ScheduleDayModel
from app.schemas.lesson import CreateScheduleDay, UpdateScheduleDay


class CRUDScheduleDay(CRUDBase[ScheduleDayModel, CreateScheduleDay, UpdateScheduleDay]):
    pass


schedule_day_crud = CRUDScheduleDay(ScheduleDayModel)
