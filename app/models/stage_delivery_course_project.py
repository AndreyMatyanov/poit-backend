from app.db.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, DateTime


class StageCourseProject(Base):
    __tablename__ = 'stage_course_project'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    course_project_id = Column(Integer, ForeignKey('course_project_base.id'))
    title = Column(String, nullable=False)
    description = Column(String)
    is_done = Column(Boolean)
    deadline_date = Column(DateTime)
