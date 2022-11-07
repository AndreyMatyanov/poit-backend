from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends import verify_admin, get_db
from app.schemas.lesson import Discipline, CreateDiscipline
from app.service import discipline_service

router = APIRouter()


@router.get('/', response_model=List[Discipline])
def get_disciplines(db: Session = Depends(get_db)):
    return discipline_service.get_all_disciplines(db=db)


@router.get('/{discipline_id}', response_model=Optional[Discipline])
def get_discipline_by_id(discipline_id: int, db: Session = Depends(get_db)):
    return discipline_service.get_by_id(db=db, discipline_id=discipline_id)


@router.post('/', response_model=Discipline)
def create_discipline(discipline_create: CreateDiscipline, db: Session = Depends(get_db), _=Depends(verify_admin)):
    return discipline_service.create_discipline(db=db, discipline_create=discipline_create)


@router.delete('/{discipline_id}', response_model=Discipline)
def delete_discipline(discipline_id: int, db: Session = Depends(get_db), _=Depends(verify_admin)) -> Discipline:
    return discipline_service.delete_discipline(db=db, discipline_id=discipline_id)
