import datetime

from sqlalchemy.orm import Session

from app.schemas.group import CreateGroup
from app.schemas.user import UserStudentCreate
from app.service import group_service, user_student_service


def test_create_group(db: Session):
    # Given
    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    # When
    group = group_service.create_group(db=db, created_group=create_group)
    # Then
    assert group.group_name == create_group.group_name
    assert group.group_number == create_group.group_number
    assert group.count_of_subgroup == create_group.count_of_subgroup


def test_get_groups(db: Session):
    # Given
    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group_service.create_group(db=db, created_group=create_group)
    # When
    groups = group_service.get_groups(db=db)
    # Then
    assert len(groups) == 1


def test_delete_group(db: Session):
    # Given
    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)
    # When
    group_service.delete_group(db=db, group_id=group.id)
    groups = group_service.get_groups(db=db)
    # Then
    assert len(groups) == 0


def test_get_group_by_id(db: Session):
    # Given
    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)
    # When
    getted_group = group_service.get_group_by_id(db=db, group_id=group.id)
    # Then
    assert getted_group.group_number == create_group.group_number
    assert getted_group.group_name == create_group.group_name
    assert getted_group.count_of_subgroup == create_group.count_of_subgroup


def test_get_students_by_group_id(db: Session):
    # Given
    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    first_student = UserStudentCreate(
        start_of_studing=datetime.datetime.now(),
        number_of_ticket=1111,
        group_id=group.id,
        subgroup=1,
        email="test1@gmail.com",
        name='Валерия',
        surname='Язагит',
        second_name='Александровна',
        password='12345678'
    )

    second_student = UserStudentCreate(
        start_of_studing=datetime.datetime.now(),
        number_of_ticket=1112,
        group_id=group.id,
        subgroup=1,
        email="test2@gmail.com",
        name='Садао',
        surname='Мао',
        second_name='Кирг',
        password='12345678'
    )
    user_student_service.create_user_student(db=db, user_student_create=first_student)
    user_student_service.create_user_student(db=db, user_student_create=second_student)
    # When
    students = group_service.get_students_by_group_id(db=db, group_id=group.id)
    # Then
    assert len(students) == 2

