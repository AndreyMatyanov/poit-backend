from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean, BigInteger
from sqlalchemy.orm import relationship

from app.models.users import User
from app.models.group import Group


class UserStudent(User):
    __tablename__ = "user_student"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    start_of_studing = Column(DateTime, nullable=False)
    number_of_ticket = Column(BigInteger, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'))
    subgroup = Column(Integer, nullable=False)

    __mapper_args__ = {'polymorphic_identity': 'STUDENT', 'polymorphic_load': 'inline'}
    group = relationship('Group', foreign_keys=[group_id], primaryjoin='Group.id == UserStudent.group_id')
