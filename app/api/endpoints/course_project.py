from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends import verify_admin, get_db
from app.schemas.course_project import CreateCourseProjectRequest, CreateCourseProjectForGroupRequest, CourseProjectBase
from app.service import course_project_service

router = APIRouter()


@router.post('/')
def create_course_project_for_student(create_project: CreateCourseProjectRequest, db: Session = Depends(get_db),
                                      _=Depends(verify_admin)):
    course_project = course_project_service.create_course_project(db=db, create_project=create_project)
    return course_project


@router.post('/create-for-group/')
def create_course_project_for_group(create_projects: CreateCourseProjectForGroupRequest, db: Session = Depends(get_db),
                                    _=Depends(verify_admin)):
    courses_projects = course_project_service.create_course_projects_for_group(
        db=db,
        create_projects_request=create_projects)
    return courses_projects


@router.get('/{id}')
def get_course_project_by_id(project_id: int, db: Session = Depends(get_db)):
    course_project: Optional[CourseProjectBase] = course_project_service.get_course_project_by_id(db=db,
                                                                                                  project_id=project_id)
    return course_project

@router.get('/get-projects-by-student/{user_student_id}')
def get_course_projects_by_user_id(user_student_id: int, db: Session = Depends(get_db)):
    course_projects: List[CourseProjectBase] = course_project_service.get_course_projects_by_user_student_id(
        user_student_id=user_student_id,
        db=db
    )
    return course_projects