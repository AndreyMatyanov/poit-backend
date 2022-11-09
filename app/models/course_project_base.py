from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float


class CourseProjectBase(Base):
    __tablename__ = 'course_project_base'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    discipline_id = Column(Integer, ForeignKey('disciplines.id'))
    user_student_id = Column(Integer, ForeignKey('users.id'))
    percent_of_completion = Column(Float, nullable=False)

    stages = relationship("StageCourseProject", back_populates="course_project",
                             primaryjoin="StageCourseProject.course_project_id == CourseProjectBase.id",
                             lazy='joined', uselist=True)
