from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Discipline(Base):
    __tablename__ = 'disciplines'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    discipline_name = Column(String, unique=True)
    count_of_hours = Column(Integer)
    description = Column(String)
    
