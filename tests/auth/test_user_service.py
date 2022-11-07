from sqlalchemy.orm import Session

from app.schemas.user import UserTeacherCreate
from app.service import user_teacher_service, user_service


def test_get_user_by_id(db: Session):
    # Given
    create_teacher_user = UserTeacherCreate(
        email="test1@gmail.com",
        name="Иван",
        second_name="Иванов",
        surname="Иванович",
        password="12345678",
        job_title="Зав.кафедры",
        rank="Доцент"
    )
    user_cr = user_teacher_service.create_user_teacher(db=db, user_teacher_create=create_teacher_user)

    # When
    user = user_service.get_user_by_id(db=db, id=user_cr.id)

    # Then
    assert user.id == user_cr.id
    assert user.name == create_teacher_user.name
    assert user.second_name == create_teacher_user.second_name
    assert user.surname == create_teacher_user.surname
    assert user.job_title == create_teacher_user.job_title
    assert user.rank == create_teacher_user.rank


def test_delete_user_by_id(db: Session):
    # Given
    create_teacher_user = UserTeacherCreate(
        email="test1@gmail.com",
        name="Иван",
        second_name="Иванов",
        surname="Иванович",
        password="12345678",
        job_title="Зав.кафедры",
        rank="Доцент"
    )
    user_cr = user_teacher_service.create_user_teacher(db=db, user_teacher_create=create_teacher_user)
    # When
    user_service.delete_user_by_id(db=db, id=user_cr.id)
    user = user_service.get_user_by_id(db=db, id=user_cr.id)
    # Then
    assert user is None
    