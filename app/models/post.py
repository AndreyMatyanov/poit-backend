from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.users import User


class Post(Base):
    __tablename__ = "news_posts"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String)
    text = Column(String(length=2000))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))