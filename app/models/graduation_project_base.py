from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class GraduationProjectBase(Base):
    __tablename__ = "gradations_project_base"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_student_id = Column(Integer, ForeignKey('users.id'))
    theme = Column(String)
    