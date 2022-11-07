from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.models.users import User


class UserTeacher(User):
    __tablename__ = "user_teacher"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    job_title = Column(String, nullable=False)
    rank = Column(String, nullable=False)

    __mapper_args__ = {'polymorphic_identity': 'TEACHER', 'polymorphic_load': 'inline'}
