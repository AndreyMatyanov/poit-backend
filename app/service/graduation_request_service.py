import datetime
from typing import List

from sqlalchemy.orm import Session

from app.crud.graduation_request_crud import graduation_request_crud
from app.schemas.graduation_project import CreateGraduationProjectRequest, CreateGraduationProject
from app.schemas.graduation_request import GraduationRequestBase, UpdateGraduationRequest, CreateGraduationRequest, \
    StatusOfRequest
from app.service import graduation_project_service


def get_graduation_request_by_user_teacher_id(user_teacher_id: int, db: Session) -> List[GraduationRequestBase]:
    return graduation_request_crud.get_by_user_teacher_id(db=db, user_teacher_id=user_teacher_id)


def get_graduation_request_by_user_student_id(user_student_id: int, db: Session) -> List[GraduationRequestBase]:
    return graduation_request_crud.get_by_user_student_id(db=db, user_student_id=user_student_id)


def update_graduation_request(id: int, obj_update: UpdateGraduationRequest, db: Session):
    graduation_request_db = graduation_request_crud.get(db=db, id=id)
    if UpdateGraduationRequest.status == StatusOfRequest.ACCEPTED:
        graduation_project_create = CreateGraduationProjectRequest(
            create_prj_db=CreateGraduationProject(
                user_student_id=obj_update.user_student_id,
                percent_of_completion=0,
                pattern_of_education="BEL",
                theme=obj_update.theme
            ),
            user_teacher_id=obj_update.user_teacher_id,
            topic_approval_date=datetime.datetime.now(),
            topic_confirmation_date=datetime.datetime.date(datetime.datetime(datetime.date.today().year + 1, 1, 10)),
            project_completion_date=datetime.datetime.date(datetime.datetime(datetime.date.today().year + 1, 7, 20)),
            admission_project_protection_date=datetime.datetime.date(
                datetime.datetime(datetime.date.today().year + 1, 7, 30)),
            graduation_date=datetime.datetime.date(datetime.datetime(datetime.date.today().year + 1, 8, 10))
        )
        graduation_project_service.create_project(db=db, create_project_rq=graduation_project_create)
    graduation_request_crud.update(db=db, db_obj=graduation_request_db, obj_in=obj_update)
    return True


def create_graduation_request(create_obj: CreateGraduationRequest, db: Session):
    obj = graduation_request_crud.create(db=db, obj_in=create_obj)
    return obj
