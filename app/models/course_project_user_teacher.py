from sqlalchemy import Column, Integer, ForeignKey

from app.db.database import Base


class CourseProjectUserTeacher(Base):
    __tablename__ = "course_proj_user_teacher"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_teacher_id = Column(Integer, ForeignKey('users.id'))
    course_project_id = Column(Integer, ForeignKey('course_project_base.id'))
