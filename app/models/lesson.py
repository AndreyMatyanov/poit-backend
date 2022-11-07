from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship

from app.models.group import Group
from app.models.discipline import Discipline
from app.models.users import User
from app.models.schedule_day import ScheduleDay
from app.db.database import Base


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    user_teacher_id = Column(Integer, ForeignKey('users.id'))
    type_of_lesson = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    discipline_id = Column(Integer, ForeignKey('disciplines.id'))
    schedule_day_id = Column(Integer, ForeignKey('schedule_days.id'))
    subgroup = Column(Integer)
    cabinet = Column(String)

    schedule_day = relationship(
        'ScheduleDay',
        foreign_keys=[schedule_day_id],
        primaryjoin='ScheduleDay.id == Lesson.schedule_day_id'
    )
    group = relationship(
        'Group',
        foreign_keys=[group_id],
        primaryjoin='Group.id == Lesson.group_id'
    )
    user_teacher = relationship(
        'User',
        foreign_keys=[user_teacher_id],
        primaryjoin='User.id == Lesson.user_teacher_id'
    )
    discipline = relationship(
        'Discipline',
        foreign_keys=[discipline_id],
        primaryjoin='Discipline.id == Lesson.discipline_id'
    )
