from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends import get_db
from app.schemas.graduation_request import UpdateGraduationRequest, CreateGraduationRequest
from app.service import graduation_request_service

router = APIRouter()


@router.get('/get-by-user-teacher-id/{user_teacher_id}')
def get_request_by_user_teacher_id(user_teacher_id: int, db: Session = Depends(get_db)):
    requests = graduation_request_service.get_graduation_request_by_user_teacher_id(db=db,
                                                                                    user_teacher_id=user_teacher_id)
    return requests


@router.get('/get-by-user-student-id/{user_student_id}')
def get_request_by_user_student_id(user_student_id: int, db: Session = Depends(get_db)):
    requests = graduation_request_service.get_graduation_request_by_user_student_id(db=db,
                                                                                    user_student_id=user_student_id)
    return requests


@router.put('/{user_id}')
def update_graduation_request(user_id: int, obj_update: UpdateGraduationRequest, db: Session = Depends(get_db)):
    project = graduation_request_service.update_graduation_request(db=db, obj_update=obj_update, id=user_id)
    return project


@router.post('/')
def create_graduation_request(obj_create: CreateGraduationRequest, db: Session = Depends(get_db)):
    project = graduation_request_service.create_graduation_request(create_obj=obj_create, db=db)
    return project
