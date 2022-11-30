import json
import uuid
from typing import Optional, List
from uuid import UUID

from pydantic import parse_obj_as
from sqlalchemy import select
from sqlalchemy.orm import Session, with_polymorphic

from app.config.security import get_random_string, hash_password
from app.crud.user_crud import user_crud
from app.models.tokens import UserSession
from app.models.users import User
from app.models.user_teacher import UserTeacher as UserTeacherModel
from app.schemas.user import UserCreate, UserTeacherCreate, UserTeacher, RoleType, UserStudent
from app.schemas.user import TokenBase
from datetime import datetime, timedelta

tournament_se_model = with_polymorphic(User, [UserTeacherModel])


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).one_or_none()


def get_all_users(db: Session) -> List[User]:
    return user_crud.get_multi(db=db)


def get_user_by_token(db: Session, token: str):
    response = db.query(UserSession).join(User).filter(UserSession.token == token).one_or_none()
    return response


def create_user_token(db: Session, user_id: int, roles: list):
    token = UserSession(
        token=uuid.uuid4(),
        expires=datetime.now() + timedelta(weeks=2),
        user_id=user_id
    )
    db.add(token)
    db.commit()
    db.refresh(token)
    return token


def create_user(db: Session, user: UserCreate):
    salt = get_random_string()
    hashed_password = hash_password(user.password, salt)
    user.password = hashed_password
    user_model = User(
        name=user.name,
        surname=user.surname,
        second_name=user.second_name,
        hashed_password=hashed_password,
        email=user.email,
        is_active=False
    )
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    token = create_user_token(db=db, user_id=user_model.id)

    token_dict = TokenBase.from_orm(token)
    return {**user.dict(), "id": token.user_id, "is_active": True, "token": token_dict}


def get_user_by_id(db: Session, id: int) -> Optional[UserTeacher | UserStudent]:
    user: Optional[User] = user_crud.get_user_by_id(db=db, user_id=id)
    if user is None:
        return None
    if user.role == RoleType.TEACHER:
        return parse_obj_as(UserTeacher, user)
    elif user.role == RoleType.STUDENT:
        return parse_obj_as(UserStudent, user)
    return user


def delete_user_by_id(db: Session, id: int):
    return user_crud.remove(db=db, id=id)


def get_by_role(role: RoleType, db: Session):
    return user_crud.get_users_by_role(db=db, role=role)
