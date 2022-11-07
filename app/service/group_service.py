from typing import List

from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.crud.group_crud import group_crud
from app.crud.student_user import user_student_crud
from app.schemas.group import GroupBase, CreateGroup
from app.schemas.user import UserStudent


def get_groups(db: Session) -> List[GroupBase]:
    return group_crud.get_multi(db=db)


def create_group(db: Session, created_group: CreateGroup):
    return group_crud.create(db=db, obj_in=created_group.__dict__)


def delete_group(db: Session, group_id: int):
    return group_crud.remove(db=db, id=group_id)


def get_students_by_group_id(db: Session, group_id: int) -> List[UserStudent]:
    user_students_db: List[UserStudent] = user_student_crud.get_users_students_by_group_id(db=db, group_id=group_id)
    return [UserStudent.from_orm(user_student_db) for user_student_db in user_students_db]


def get_group_by_id(db: Session, group_id: int) -> GroupBase:
    group_db = group_crud.get(db=db, id=group_id)
    return parse_obj_as(GroupBase, group_db)
