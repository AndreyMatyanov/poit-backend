from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import sqlalchemy

from app.db.database import Base
from app.models.users import User


class UserSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    token = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        index=True
    )
    expires = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user = relationship('User', foreign_keys=[user_id], primaryjoin='User.id == UserSession.user_id')
