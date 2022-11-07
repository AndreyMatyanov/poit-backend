from typing import List

from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.config.security import get_random_string, hash_password
from app.crud.student_user import user_student_crud
from app.schemas.user import UserStudent, RoleType, UserBase, UserStudentCreate
from app.models.user_student import UserStudent as UserStudentModel


def create_user_student(db: Session, user_student_create: UserStudentCreate) -> UserStudent:
    salt = get_random_string()
    hashed_password = hash_password(user_student_create.password, salt)
    user_student_create_model = UserStudentModel(
        role=RoleType.STUDENT,
        start_of_studing=user_student_create.start_of_studing,
        number_of_ticket=user_student_create.number_of_ticket,
        name=user_student_create.name,
        surname=user_student_create.surname,
        second_name=user_student_create.second_name,
        email=user_student_create.email,
        group_id=user_student_create.group_id,
        subgroup=user_student_create.subgroup,
        hashed_password=hashed_password,
        is_active=False,
        is_admin=False
    )
    user_student_db: UserStudentModel = user_student_crud.create(db=db, obj_in=user_student_create_model.__dict__)
    return parse_obj_as(UserStudent, user_student_db)
