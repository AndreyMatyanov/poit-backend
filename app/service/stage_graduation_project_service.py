from datetime import datetime

from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.crud.graduation_project_crud import graduation_project_crud
from app.crud.stage_graduation_project_crud import step_graduation_project_crud
from app.schemas.graduation_project import CreateStageGraduationProject, UpdateStageGraduationProject, \
    UpdateGraduationProject, GraduationProjectBase, GraduationProjectBaseWithoutStage
from app.service import graduation_project_service


def get_stages_by_project_id(db: Session, project_id: int):
    stages_db = step_graduation_project_crud.get_stages_by_project_id(db=db, project_id=project_id)
    return stages_db


def create_step_graduation_project(db: Session, step_course_project_create: CreateStageGraduationProject):
    step = step_graduation_project_crud.create(db=db, obj_in=step_course_project_create)
    return step


def _create_base_graduation_project_base(
        db: Session,
        graduation_project_id: int,
        topic_approval_date: datetime,
        topic_confirmation_date: datetime,
        project_completion_date: datetime,
        admission_project_protection_date: datetime,
        graduation_date: datetime
):
    step = CreateStageGraduationProject(
        graduation_project_id=graduation_project_id,
        title='Согласование темы дипломного проекта',
        description='',
        is_done=False,
        deadline_date=topic_approval_date
    )
    create_step_graduation_project(db=db, step_course_project_create=step)

    step = CreateStageGraduationProject(
        graduation_project_id=graduation_project_id,
        title='Подтверждение темы дипломного проекта',
        description='',
        is_done=False,
        deadline_date=topic_confirmation_date
    )
    create_step_graduation_project(db=db, step_course_project_create=step)

    step = CreateStageGraduationProject(
        graduation_project_id=graduation_project_id,
        title='Завершение работы над проектом',
        description='',
        is_done=False,
        deadline_date=project_completion_date
    )
    create_step_graduation_project(db=db, step_course_project_create=step)

    step = CreateStageGraduationProject(
        graduation_project_id=graduation_project_id,
        title='Допуск к защите дипломного проекта',
        description='',
        is_done=False,
        deadline_date=admission_project_protection_date
    )
    create_step_graduation_project(db=db, step_course_project_create=step)

    step = CreateStageGraduationProject(
        graduation_project_id=graduation_project_id,
        title='Защита дипломного проекта',
        description='',
        is_done=False,
        deadline_date=graduation_date
    )
    create_step_graduation_project(db=db, step_course_project_create=step)


def set_is_done(db: Session, stage_id: int):
    step_db = step_graduation_project_crud.get(db=db, id=stage_id)
    update_stage = UpdateStageGraduationProject(
        graduation_project_id=step_db.graduation_project_id,
        title=step_db.title,
        description=step_db.title,
        is_done=True,
        deadline_date=step_db.deadline_date
    )
    step_graduation_project_crud.update(db=db, db_obj=step_db, obj_in=update_stage)
    _set_percent_of_complete(db=db, project_id=step_db.graduation_project_id)
    return True


def _set_percent_of_complete(db: Session, project_id: int):
    project_db = graduation_project_service.get_project_by_id(db=db, id=project_id)
    count_of_stages = len(project_db.stages)
    count_of_true = 0

    for stage in project_db.stages:
        if stage.is_done is True:
            count_of_true += 1

    project_update = UpdateGraduationProject(
        user_student_id=project_db.user_student_id,
        percent_of_completion=count_of_true / count_of_stages,
        pattern_of_education=project_db.pattern_of_education,
        theme=project_db.theme
    )

    graduation_project_crud.update(db=db, db_obj=project_db, obj_in=project_update)
