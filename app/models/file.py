from sqlalchemy import Column, Integer, String

from app.db.database import Base


class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    file_type = Column(String)
    size = Column(Integer)
    mime_type = Column(String)
    modification_time = Column(String)
