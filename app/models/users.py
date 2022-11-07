from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    surname = Column(String)
    second_name = Column(String)
    email = Column(String(40), unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_admin = Column(Boolean, nullable=False)

    __mapper_args__ = {'polymorphic_identity': 'users', 'polymorphic_on': role, 'polymorphic_load': 'inline'}
