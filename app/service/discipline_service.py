from typing import Optional

from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.crud.discipline_crud import discipline_crud
from app.schemas.lesson import Discipline, CreateDiscipline


def get_all_disciplines(db: Session):
    disciplines_db = discipline_crud.get_multi(db=db)
    return [Discipline.from_orm(discipline_db) for discipline_db in disciplines_db]


def get_by_id(db: Session, discipline_id: int) -> Optional[Discipline]:
    discipline_db = discipline_crud.get(db=db, id=discipline_id)
    if discipline_db is None:
        return None
    return parse_obj_as(Discipline, discipline_db)


def create_discipline(db: Session, discipline_create: CreateDiscipline):
    discipline_db = discipline_crud.create(db=db, obj_in=discipline_create)
    return parse_obj_as(Discipline, discipline_db)


def delete_discipline(db: Session, discipline_id: int):
    discipline_db = discipline_crud.remove(db=db, id=discipline_id)
    return parse_obj_as(Discipline, discipline_db)
