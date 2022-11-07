from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    group_number = Column(Integer)
    group_name = Column(String)
    count_of_subgroup = Column(Integer)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)
