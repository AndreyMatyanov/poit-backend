from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float


class CourseProjectBase(Base):
    __tablename__ = 'course_project_base'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    discipline_id = Column(Integer, ForeignKey('discipline.id'))
    theme = Column(String, nullable=True)
    date_selection_topic = Column(DateTime)
    percent_of_completion = Column(Float, nullable=False)


