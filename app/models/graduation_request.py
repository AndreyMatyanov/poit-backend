from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.database import Base


class GraduationRequest(Base):
    __tablename__ = 'create_graduation_request'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_student_id = Column(Integer, ForeignKey('users.id'))
    user_teacher_id = Column(Integer, ForeignKey('users.id'))
    theme = Column(String)
    description = Column(String)
    status = Column(String)
