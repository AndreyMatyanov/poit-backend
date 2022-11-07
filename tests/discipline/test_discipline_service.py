from sqlalchemy.orm import Session

from app.schemas.lesson import CreateDiscipline
from app.service import discipline_service


def test_get_disciplines(db: Session):
    # Given
    create_discipline_one = CreateDiscipline(
        discipline_name='МиСЗИ',
        count_of_hours='200',
        description='Крутой предмет'
    )

    create_discipline_two = CreateDiscipline(
        discipline_name='ЭВМиПУ',
        count_of_hours='210',
        description='Крутой предмет'
    )
    discipline_service.create_discipline(db=db, discipline_create=create_discipline_one)
    discipline_service.create_discipline(db=db, discipline_create=create_discipline_two)
    # When
    disciplines = discipline_service.get_all_disciplines(db=db)
    # Then
    assert len(disciplines)


def test_get_discipline_by_id(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='МиСЗИ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    discipline_created = discipline_service.create_discipline(db=db, discipline_create=create_discipline)

    # When
    discipline = discipline_service.get_by_id(db=db, discipline_id=discipline_created.id)
    # Then
    assert discipline.id == discipline_created.id
    assert discipline.discipline_name == create_discipline.discipline_name
    assert discipline.count_of_hours == create_discipline.count_of_hours
    assert discipline.description == create_discipline.description


def test_create_discipline(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='ЭВМиПУ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    # When
    discipline_created = discipline_service.create_discipline(db=db, discipline_create=create_discipline)
    # Then
    assert discipline_created.discipline_name == create_discipline.discipline_name
    assert discipline_created.count_of_hours == create_discipline.count_of_hours
    assert discipline_created.description == create_discipline.description


def test_delete_discipline(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='МиСЗИ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    discipline_created = discipline_service.create_discipline(db=db, discipline_create=create_discipline)
    # When
    discipline_service.delete_discipline(db=db, discipline_id=discipline_created.id)
    search_discipline = discipline_service.get_by_id(db=db, discipline_id=discipline_created.id)
    # Then
    assert search_discipline is None
