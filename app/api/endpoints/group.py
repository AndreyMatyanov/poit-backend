from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends import get_db, verify_admin
from app.schemas.group import GroupBase, CreateGroup
from app.service import group_service, user_student_service

router = APIRouter()


@router.get('/')
def get_groups(db: Session = Depends(get_db)):
    groups: List[GroupBase] = group_service.get_groups(db=db)
    return groups


@router.post('/')
def create_group(created_group: CreateGroup, db: Session = Depends(get_db), _=Depends(verify_admin)):
    return group_service.create_group(db=db, created_group=created_group)


@router.delete('/{group_id}')
def delete_group(group_id: int, db: Session = Depends(get_db), _=Depends(verify_admin)):
    return group_service.delete_group(db=db, group_id=group_id)


@router.get('/student-list/{group_id}')
def get_students_by_group_id(group_id: int, db: Session = Depends(get_db)):
    return group_service.get_students_by_group_id(db=db, group_id=group_id)


@router.get('/{group_id}')
def get_group_by_id(group_id: int, db: Session = Depends(get_db)):
    return group_service.get_group_by_id(group_id=group_id, db=db)
