from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.config.security import get_random_string, hash_password
from app.crud.teacher_user import user_teacher_crud
from app.schemas.user import UserTeacherCreate, UserTeacher, RoleType, User, UserBase
from app.models.user_teacher import UserTeacher as UserTeacherModel


def create_user_teacher(db: Session, user_teacher_create: UserTeacherCreate) -> UserBase:
    salt = get_random_string()
    hashed_password = hash_password(user_teacher_create.password, salt)
    user_teacher_create_model = UserTeacherModel(
        role=RoleType.TEACHER,
        job_title=user_teacher_create.job_title,
        rank=user_teacher_create.rank,
        name=user_teacher_create.name,
        surname=user_teacher_create.surname,
        second_name=user_teacher_create.second_name,
        email=user_teacher_create.email,
        hashed_password=hashed_password,
        is_active=False,
        is_admin=False
    )
    user_teacher_db: UserTeacherModel = user_teacher_crud.create(db=db, obj_in=user_teacher_create_model.__dict__)
    return parse_obj_as(UserTeacher, user_teacher_db)
