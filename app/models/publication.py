from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.file import File


class Publication(Base):
    __tablename__ = 'publications'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    file_id = Column(Integer, ForeignKey('files.id'))
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    publication_type = Column(String, nullable=False)
    description = Column(String)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    file = relationship('File', foreign_keys=[file_id], primaryjoin='File.id == Publication.file_id')
