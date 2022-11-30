from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends import get_db, verify_admin
from app.schemas.graduation_project import GraduationProjectBase, CreateGraduationProjectForGroupRequest, \
    CreateGraduationProject, CreateGraduationProjectRequest, UpdateGraduationProject, TeacherProject
from app.service import graduation_project_service

router = APIRouter()


@router.get('/', response_model=List[GraduationProjectBase])
def get_graduation_projects_all(db: Session = Depends(get_db)):
    return graduation_project_service.get_all_projects(db=db)


@router.post('/create-for-group/')
def create_project_for_group(create_projects: CreateGraduationProjectForGroupRequest, db: Session = Depends(get_db),
                             _=Depends(verify_admin)):
    projects = graduation_project_service.create_projects_for_group(
        db=db,
        create_projects_request=create_projects)
    return projects


@router.post('/')
def create_project(create_project: CreateGraduationProjectRequest, db: Session = Depends(get_db)):
    project = graduation_project_service.create_project(db=db, create_project_rq=create_project)
    return project


@router.get('/get-by-user-id/{user_id}')
def get_by_user_student(user_id: int, db: Session = Depends(get_db)):
    project = graduation_project_service.get_project_by_user_id(db=db, user_id=user_id)
    return project


@router.get('/get-by-user-teacher-id/{user_id}', response_model=List[GraduationProjectBase])
def get_by_user_teacher(user_id: int, db: Session = Depends(get_db)):
    projects = graduation_project_service.get_by_user_teacher_id(db=db, user_id=user_id)
    return projects


@router.put('/{id}')
def update_diplome(id: int, obj_update: UpdateGraduationProject, db: Session = Depends(get_db)):
    project = graduation_project_service.update_project(db=db, obj_up=obj_update, id=id)
    return project


@router.get('/get-all-teachers-projects', response_model=List[TeacherProject])
def get_all_teachers_projects(db: Session = Depends(get_db)):
    obj = graduation_project_service.get_all_teachers_projects(db=db)
    return obj
