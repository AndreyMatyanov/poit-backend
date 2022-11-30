from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.graduation_request import GraduationRequest
from app.schemas.graduation_request import CreateGraduationRequest, UpdateGraduationRequest, StatusOfRequest


class CRUDGraduationRequest(CRUDBase[GraduationRequest, CreateGraduationRequest, UpdateGraduationRequest]):
    def get_by_user_teacher_id(self, db: Session, user_teacher_id: int):
        requests_db = db.query(self.model).filter(self.model.user_teacher_id == user_teacher_id).filter(
            self.model.status == StatusOfRequest.WAITING).all()
        return requests_db

    def get_by_user_student_id(self, db: Session, user_student_id: int):
        requests_db = db.query(self.model).filter(self.model.user_student_id == user_student_id).filter(
            self.model.status == StatusOfRequest.WAITING).all()
        return requests_db


graduation_request_crud = CRUDGraduationRequest(GraduationRequest)
