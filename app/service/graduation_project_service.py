from typing import Optional, List, Union

from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.crud.count_of_teachers_projects_crud import course_project_user_teacher_crud
from app.crud.graduation_project_crud import graduation_project_crud
from app.crud.graduation_project_user_teacher_crud import graduation_project_user_teacher_crud
from app.schemas.count_of_teachers_project import CreateCountOfTeacherProject, CountOfTeacherProjectBase
from app.schemas.graduation_project import CreateGraduationProjectForGroupRequest, CreateGraduationProjectRequest, \
    GraduationProjectBase, CreateGraduationProject, UpdateGraduationProject, TeacherProject, StageGraduationProjectBase
from app.schemas.user import RoleType
from app.service import user_service
from app.service.group_service import get_students_by_group_id
from app.service.stage_graduation_project_service import _create_base_graduation_project_base


def get_all_projects(db: Session):
    return graduation_project_crud.get_multi(db=db)


def get_project_by_id(db: Session, id: int):
    project_db = graduation_project_crud.get(db=db, id=id)
    return project_db


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


def update_project(db: Session, obj_up: UpdateGraduationProject, id: int):
    project_db = get_project_by_id(db=db, id=id)
    graduation_project_crud.update(db=db, db_obj=project_db, obj_in=obj_up)
    return True


def get_project_by_user_id(db: Session, user_id: int) -> Optional[GraduationProjectBase]:
    project_db = graduation_project_crud.get_by_user_id(db=db, user_id=user_id)
    if project_db is None:
        return None
    return parse_obj_as(GraduationProjectBase, project_db)


def get_by_user_teacher_id(db: Session, user_id: int) -> List[GraduationProjectBase]:
    projects_user_teacher = graduation_project_user_teacher_crud.get_by_user_id(db=db, user_id=user_id)
    projects: Union[GraduationProjectBase, List[GraduationProjectBase]] = []
    for project_user_teacher in projects_user_teacher:
        project_db = get_project_by_id(db=db, id=project_user_teacher.graduation_project_id)
        print(project_db.user.name)
        projects.append(project_db)
    return projects


def get_all_teachers_projects(db: Session) -> List[TeacherProject]:
    users = user_service.get_by_role(role=RoleType.TEACHER, db=db)
    teacher_project_list: List[TeacherProject] = []
    for user in users:
        projects = get_by_user_teacher_id(db=db, user_id=user.id)
        teacher_project = TeacherProject(
            user_teacher=user,
            projects=projects
        )
        teacher_project_list.append(teacher_project)
    return teacher_project_list


def get_count_of_teachers_projects(db: Session):
    objs = course_project_user_teacher_crud.get_multi(db=db)
    return [CountOfTeacherProjectBase.from_orm(obj) for obj in objs]


def create_count_of_teacher_projects(db: Session, create_obj: CreateCountOfTeacherProject):
    obj = course_project_user_teacher_crud.create(db=db, obj_in=create_obj)
    return obj
