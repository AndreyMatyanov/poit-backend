from typing import List

from sqlalchemy.orm import Session

from app.crud.graduation_request_crud import graduation_request_crud
from app.schemas.graduation_request import GraduationRequestBase, UpdateGraduationRequest, CreateGraduationRequest


def get_graduation_request_by_user_teacher_id(user_teacher_id: int, db: Session) -> List[GraduationRequestBase]:
    return graduation_request_crud.get_by_user_teacher_id(db=db, user_teacher_id=user_teacher_id)


def get_graduation_request_by_user_student_id(user_student_id: int, db: Session) -> List[GraduationRequestBase]:
    return graduation_request_crud.get_by_user_student_id(db=db, user_student_id=user_student_id)


def update_graduation_request(id: int, obj_update: UpdateGraduationRequest, db: Session):
    graduation_request_db = graduation_request_crud.get(db=db, id=id)
    graduation_request_crud.update(db=db, db_obj=graduation_request_db, obj_in=obj_update)
    return True


def create_graduation_request(create_obj: CreateGraduationRequest, db: Session):
    obj = graduation_request_crud.create(db=db, obj_in=create_obj)
    return obj
