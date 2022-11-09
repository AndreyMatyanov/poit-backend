from typing import List

from pydantic import parse_obj_as
from requests import Session

from app.crud.course_project_crud import course_project_crud
from app.crud.course_project_user_teacher_crud import course_project_user_teacher_crud
from app.schemas.course_project import CreateCourseProject, CreateCourseProjectRequest, \
    CreateCourseProjectForGroupRequest, CreateCourseProjectUserTeacher, CourseProjectBase
from app.service.group_service import get_students_by_group_id
from app.service.step_course_project import _create_base_course_project_base


def create_course_project(db: Session, create_project: CreateCourseProjectRequest):
    course_project = course_project_crud.create(db=db, obj_in=create_project.create_course_prj_db)

    _create_base_course_project_base(
        db=db,
        course_project_id=course_project.id,
        topic_approval_date=create_project.topic_approval_date,
        topic_confirmation_date=create_project.topic_confirmation_date,
        project_completion_date=create_project.project_completion_date,
        admission_project_protection_date=create_project.admission_project_protection_date,
        graduation_date=create_project.graduation_date
    )

    course_project_user_teacher = CreateCourseProjectUserTeacher(
        user_teacher_id=create_project.user_teacher_id,
        course_project_id=course_project.id
    )
    course_project_user_teacher_crud.create(db=db, obj_in=course_project_user_teacher)
    return course_project


def create_course_projects_for_group(db: Session, create_projects_request: CreateCourseProjectForGroupRequest):
    users_students = get_students_by_group_id(db=db, group_id=create_projects_request.group_id)
    projects: List = []
    for user_student in users_students:
        course_project_create = CreateCourseProject(
            discipline_id=create_projects_request.discipline_id,
            user_student_id=user_student.id,
            percent_of_completion=0
        )

        course_project = course_project_crud.create(db=db, obj_in=course_project_create)

        _create_base_course_project_base(
            db=db,
            course_project_id=course_project.id,
            topic_approval_date=create_projects_request.topic_approval_date,
            topic_confirmation_date=create_projects_request.topic_confirmation_date,
            project_completion_date=create_projects_request.project_completion_date,
            admission_project_protection_date=create_projects_request.admission_project_protection_date,
            graduation_date=create_projects_request.graduation_date
        )
        course_project_user_teacher = CreateCourseProjectUserTeacher(
            user_teacher_id=create_projects_request.user_teacher_id,
            course_project_id=course_project.id
        )
        course_project_user_teacher_crud.create(db=db, obj_in=course_project_user_teacher)
        projects.append(course_project)
    return projects


def get_course_project_by_id(db: Session, project_id: int):
    course_project_db = course_project_crud.get(db=db, id=project_id)
    if course_project_db is None:
        print('lol')
        return None
    return parse_obj_as(CourseProjectBase, course_project_db)


def get_course_projects_by_user_student_id(db: Session, user_student_id):
    course_projects_db = course_project_crud.get_projects_by_user_student_id(db=db, user_student_id=user_student_id)
    return [CourseProjectBase.from_orm(course_project_db) for course_project_db in course_projects_db]