from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends import get_db
from app.schemas.graduation_project import StageGraduationProjectBase, CreateStageGraduationProject, \
    UpdateStageGraduationProject
from app.service import stage_graduation_project_service

router = APIRouter()


@router.get("/{project_id}")
def get_stages_by_project_id(project_id: int, db: Session = Depends(get_db)):
    stages: List[StageGraduationProjectBase] = stage_graduation_project_service.get_stages_by_project_id(
        db=db,
        project_id=project_id
    )
    return stages


@router.post("/")
def create_stage(cr_stage: CreateStageGraduationProject, db: Session = Depends(get_db)):
    stage = stage_graduation_project_service.create_step_graduation_project(step_course_project_create=cr_stage, db=db)
    return stage


@router.post('/set-is_done/{stage_id}')
def set_stage_is_done(stage_id: int, db: Session = Depends(get_db)):
    stage = stage_graduation_project_service.set_is_done(db=db, stage_id=stage_id)
    return stage


@router.put("/{stage_id}")
def update_stage(stage_id: int, obj_upd: UpdateStageGraduationProject, db: Session = Depends(get_db)):
    stage = stage_graduation_project_service.update(db=db, id=stage_id, obj_upd=obj_upd)
    return stage
