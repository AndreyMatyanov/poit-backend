from sqlalchemy import Column, Integer, DateTime, ForeignKey, String

from app.db.database import Base


class ScheduleDay(Base):
    __tablename__ = 'schedule_days'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    week_type = Column(String)
    day = Column(String)
    time = Column(String)
