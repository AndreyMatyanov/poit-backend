from typing import Optional, List

from fastapi import APIRouter, Depends
from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.api.depends import get_db, exchange_token
from app.schemas import user
from app.schemas.session import UserSession
from app.schemas.user import User, UserTeacher, UserStudent, RoleType
from app.service import user_service

router = APIRouter()


@router.get("/me")
async def read_users_me(db: Session = Depends(get_db), current_user: UserSession = Depends(exchange_token)):
    return user_service.get_user_by_id(db=db, id=current_user.user_id)


@router.get('/')
async def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db=db)


@router.post("/me")
def update_my_user():
    pass


@router.get("/{id}")
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user: Optional[UserTeacher] | Optional[UserStudent] = user_service.get_user_by_id(db=db, id=id)
    return user


@router.get("/get-by-role/{role}")
def get_teachers(role: RoleType, db: Session = Depends(get_db)):
    users_db: List = user_service.get_by_role(db=db, role=role)
    users: List[UserTeacher | UserStudent] = []
    for user_db in users_db:
        if user_db.role == RoleType.TEACHER:
            user_obj = parse_obj_as(UserTeacher, user_db)
            users.append(user_obj)
        elif user_db.role == RoleType.STUDENT:
            user_obj = parse_obj_as(UserStudent, user_db)
            users.append(user_obj)
    return users


@router.delete("/{id}")
def delete_user_by_id(id: int, db: Session = Depends(get_db)):
    user: Optional[UserTeacher] | Optional[UserStudent] = user_service.delete_user_by_id(db=db, id=id)
    return user


@router.post("/{id}")
def update_user_by_id():
    pass
