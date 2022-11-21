from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class GraduationProjectUserTeacher(Base):
    __tablename__ = 'grad_project_user_teacher'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_teacher_id = Column(Integer, ForeignKey('users.id'))
    graduation_project_id = Column(Integer, ForeignKey('graduations_project_base.id'))
