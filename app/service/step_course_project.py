from datetime import datetime

from sqlalchemy.orm import Session

from app.crud.stage_course_project_crud import step_course_project_crud
from app.schemas.course_project import CreateStageCourseProject


def create_step_course_project(db: Session, step_course_project_create: CreateStageCourseProject):
    step = step_course_project_crud.create(db=db, obj_in=step_course_project_create)
    return step


def _create_base_course_project_base(
        db: Session,
        course_project_id: int,
        topic_approval_date: datetime,
        topic_confirmation_date: datetime,
        project_completion_date: datetime,
        admission_project_protection_date: datetime,
        graduation_date: datetime
):
    step = CreateStageCourseProject(
        course_project_id=course_project_id,
        title='Согласование темы курсового проекта',
        description='',
        is_done=False,
        deadline_date=topic_approval_date
    )
    create_step_course_project(db=db, step_course_project_create=step)

    step = CreateStageCourseProject(
        course_project_id=course_project_id,
        title='Подтверждение темы курсового проекта',
        description='',
        is_done=False,
        deadline_date=topic_confirmation_date
    )
    create_step_course_project(db=db, step_course_project_create=step)

    step = CreateStageCourseProject(
        course_project_id=course_project_id,
        title='Завершение работы над проектом',
        description='',
        is_done=False,
        deadline_date=project_completion_date
    )
    create_step_course_project(db=db, step_course_project_create=step)

    step = CreateStageCourseProject(
        course_project_id=course_project_id,
        title='Допуск к защите курсового проекта',
        description='',
        is_done=False,
        deadline_date=admission_project_protection_date
    )
    create_step_course_project(db=db, step_course_project_create=step)

    step = CreateStageCourseProject(
        course_project_id=course_project_id,
        title='Защита курсового проекта',
        description='',
        is_done=False,
        deadline_date=graduation_date
    )
    create_step_course_project(db=db, step_course_project_create=step)

