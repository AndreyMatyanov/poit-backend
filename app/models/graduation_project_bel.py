from app.models.graduation_project_base import GraduationProjectBase
from sqlalchemy import Column, Integer, ForeignKey


class GraduationProjectBel(GraduationProjectBase):
    __tablename__ = 'gradation_project_bel'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)