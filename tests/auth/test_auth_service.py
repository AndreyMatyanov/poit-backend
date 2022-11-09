import datetime

from sqlalchemy.orm import Session

from app.config.security import validate_password
from app.schemas.group import CreateGroup
from app.schemas.user import UserTeacherCreate, UserStudentCreate, RoleType
from app.service import user_teacher_service, user_student_service, user_service, group_service


def test_create_teacher_user(db: Session):
    # Given
    user_teacher_create = UserTeacherCreate(
        job_title="Лаборант",
        rank="Дипломат",
        email="test1@gmail.com",
        name="Гена",
        surname="Цидармян",
        second_name="Абрахамович",
        password="12345678"
    )
    # When
    user = user_teacher_service.create_user_teacher(db=db, user_teacher_create=user_teacher_create)
    # Then
    assert user.name == user_teacher_create.name
    assert user.surname == user_teacher_create.surname
    assert user.second_name == user_teacher_create.second_name
    assert user.email == user_teacher_create.email


def test_create_student_user(db: Session):
    # Given

    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    user_student_create = UserStudentCreate(
        email="test2@gmail.com",
        name="Александр",
        surname="Невский",
        second_name="Андреевич",
        password="12345678",
        start_of_studing=datetime.datetime.now(),
        number_of_ticket=11111,
        group_id=group.id,
        subgroup=1
    )
    # When
    user = user_student_service.create_user_student(db=db, user_student_create=user_student_create)
    # Then
    assert user.name == user_student_create.name
    assert user.surname == user_student_create.surname
    assert user.second_name == user_student_create.second_name
    assert user.email == user_student_create.email


def test_auth(db: Session):
    # Given
    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    user_student_create = UserStudentCreate(
        email="test2@gmail.com",
        name="Александр",
        surname="Невский",
        second_name="Андреевич",
        password="12345678",
        start_of_studing=datetime.datetime.now(),
        number_of_ticket=11112,
        group_id=group.id,
        subgroup=1
    )
    user_student_service.create_user_student(db=db, user_student_create=user_student_create)
    # When
    user = user_service.get_user_by_email(db=db, email=user_student_create.email)
    is_validate = validate_password(password=user_student_create.password, hashed_password=user.hashed_password)
    token = user_service.create_user_token(db=db, user_id=user.id, roles=[user.role])
    # Then
    assert is_validate is True
    assert token.user.email == user_student_create.email
    assert token.user.id == user.id
    assert token.token is not None
