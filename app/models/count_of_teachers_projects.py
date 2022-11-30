from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float


class CountOfTeachersProjects(Base):
    __tablename__ = 'count_of_teachers_projects'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_teacher_id = Column(Integer, ForeignKey('users.id'), unique=True)
    max_count = Column(Integer)
    user = relationship('User', foreign_keys=[user_teacher_id],
                        primaryjoin='User.id == CountOfTeachersProjects.user_teacher_id')
