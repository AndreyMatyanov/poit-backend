from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy import select, update, desc, asc, func

from app.crud.base import CRUDBase
from app.models.graduation_project_base import GraduationProjectBase
from app.schemas.graduation_project import CreateGraduationProject, UpdateGraduationProject


class CRUDGraduationProject(CRUDBase[GraduationProjectBase, CreateGraduationProject, UpdateGraduationProject]):
    def get_by_user_id(self, db: Session, user_id: int):
        project_db = db.query(self.model).filter(self.model.user_student_id == user_id).one_or_none()
        return project_db


graduation_project_crud = CRUDGraduationProject(GraduationProjectBase)
