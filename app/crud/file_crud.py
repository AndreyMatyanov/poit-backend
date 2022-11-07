from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.file import File
from app.schemas.file import CreateFile, UpdateFile


class CRUDFile(CRUDBase[File, CreateFile, UpdateFile]):
    def get_file_from_db(self, db: Session, file_id: int):
        return db.query(self.model).filter(self.model.id == file_id).one_or_none()

    def get_file_by_name(self, db: Session, file_name: str):
        return db.query(self.model).filter(self.model.name == file_name).one_or_none()


file_crud = CRUDFile(File)
