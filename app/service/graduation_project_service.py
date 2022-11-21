from typing import Optional, List

from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.crud.graduation_project_crud import graduation_project_crud
from app.schemas.graduation_project import CreateGraduationProjectForGroupRequest, CreateGraduationProjectRequest, \
    GraduationProjectBase, CreateGraduationProject, UpdateGraduationProject
from app.service.group_service import get_students_by_group_id
from app.service.stage_graduation_project_service import _create_base_graduation_project_base


def get_all_projects(db: Session):
    return graduation_project_crud.get_multi(db=db)


def get_project_by_id(db: Session, id: int):
    return graduation_project_crud.get(db=db, id=id)


def create_projects_for_group(db: Session, create_projects_request: CreateGraduationProjectForGroupRequest):
    users_students = get_students_by_group_id(db=db, group_id=create_projects_request.group_id)
    projects: List[GraduationProjectBase] = []

    for user_student in users_students:
        graduation_project_create = CreateGraduationProject(
            user_student_id=user_student.id,
            pattern_of_education=create_projects_request.pattern_of_education
        )

        graduation_project = graduation_project_crud.create(db=db, obj_in=graduation_project_create)

        _create_base_graduation_project_base(
            db=db,
            graduation_project_id=graduation_project.id,
            topic_approval_date=create_projects_request.topic_approval_date,
            topic_confirmation_date=create_projects_request.topic_confirmation_date,
            project_completion_date=create_projects_request.project_completion_date,
            admission_project_protection_date=create_projects_request.admission_project_protection_date,
            graduation_date=create_projects_request.graduation_date
        )

        projects.append(graduation_project)
    return projects


def create_project(db: Session, create_project_rq: CreateGraduationProjectRequest):
    project = graduation_project_crud.create(db=db, obj_in=create_project_rq.create_prj_db)

    _create_base_graduation_project_base(
        db=db,
        graduation_project_id=project.id,
        topic_approval_date=create_project_rq.topic_approval_date,
        topic_confirmation_date=create_project_rq.topic_confirmation_date,
        project_completion_date=create_project_rq.project_completion_date,
        admission_project_protection_date=create_project_rq.admission_project_protection_date,
        graduation_date=create_project_rq.graduation_date
    )


def update_project(db: Session, obj_up: UpdateGraduationProject):
    project_db = get_project_by_user_id(db=db, user_id=obj_up.user_student_id)
    graduation_project_crud.update(db=db, db_obj=project_db, obj_in=obj_up)
    return True


def get_project_by_user_id(db: Session, user_id: int) -> Optional[GraduationProjectBase]:
    project_db = graduation_project_crud.get_by_user_id(db=db, user_id=user_id)
    if project_db is None:
        return None
    return parse_obj_as(GraduationProjectBase, project_db)
