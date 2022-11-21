from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base


class StageGraduationProject(Base):
    __tablename__ = 'stage_graduation_project'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    graduation_project_id = Column(Integer, ForeignKey('graduations_project_base.id'))
    title = Column(String, nullable=False)
    description = Column(String)
    is_done = Column(Boolean)
    deadline_date = Column(DateTime)

