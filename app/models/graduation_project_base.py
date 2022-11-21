from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class GraduationProjectBase(Base):
    __tablename__ = "graduations_project_base"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_student_id = Column(Integer, ForeignKey('users.id'))
    pattern_of_education = Column(String, nullable=False)
    percent_of_completion = Column(Float, nullable=False)
    theme = Column(String)

    stages = relationship("StageGraduationProject",
                          order_by="asc(StageGraduationProject.deadline_date)",
                          primaryjoin="StageGraduationProject.graduation_project_id == GraduationProjectBase.id",
                          lazy='joined', uselist=True)
