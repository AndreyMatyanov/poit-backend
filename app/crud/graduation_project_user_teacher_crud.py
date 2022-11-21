from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.graduation_project_user_teacher_id import GraduationProjectUserTeacher
from app.schemas.graduation_project import CreateGraduationProjectUserTeacher, UpdateGraduationProjectUserTeacher


class CRUDGraduationProjectUserTeacher(CRUDBase[GraduationProjectUserTeacher, CreateGraduationProjectUserTeacher, UpdateGraduationProjectUserTeacher]):
    def get_by_user_id(self, db: Session, user_id: int):
        projects_user_teacher = db.query(self.model).filter(self.model.user_teacher_id == user_id).all()
        return projects_user_teacher


graduation_project_user_teacher_crud = CRUDGraduationProjectUserTeacher(GraduationProjectUserTeacher)
