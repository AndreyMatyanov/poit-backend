from sqlalchemy.orm import Session

from app.schemas.group import CreateGroup
from app.schemas.lesson import CreateDiscipline, CreateScheduleDay, WeekType, Days, Time, CreateLesson
from app.schemas.user import UserTeacherCreate
from app.service import discipline_service, user_teacher_service, group_service, schedule_day_service, lesson_service


def test_get_all_lesson(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='ЭВМиПУ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    discipline = discipline_service.create_discipline(db=db, discipline_create=create_discipline)

    user_teacher_create = UserTeacherCreate(
        job_title="Ст.преподаватель",
        rank="Кандидат наук",
        email="prv58@bk.ru",
        name="Василий",
        surname="Прудников",
        second_name="Милайлович",
        password="12345678"
    )
    user = user_teacher_service.create_user_teacher(db=db, user_teacher_create=user_teacher_create)

    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    schedule_day_create = CreateScheduleDay(
        week_type=WeekType.UP,
        day=Days.MONDAY,
        time=Time.FIFTH
    )
    schedule_day = schedule_day_service.create_schedule_day(db=db, schedule_day_create=schedule_day_create)
    create_lesson = CreateLesson(
        discipline_id=discipline.id,
        user_teacher_id=user.id,
        group_id=group.id,
        schedule_day_id=schedule_day.id,
        subgroup=1,
        cabinet="416/2"
    )
    lesson = lesson_service.create_lesson(db=db, lesson_create=create_lesson)
    # When
    lessons = lesson_service.get_all_lessons(db=db)
    # Then
    assert len(lessons) == 1


def test_get_lessons_by_teacher_id(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='ЭВМиПУ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    discipline = discipline_service.create_discipline(db=db, discipline_create=create_discipline)

    user_teacher_create = UserTeacherCreate(
        job_title="Ст.преподаватель",
        rank="Кандидат наук",
        email="prv59@bk.ru",
        name="Василий",
        surname="Прудников",
        second_name="Милайлович",
        password="12345678"
    )
    user = user_teacher_service.create_user_teacher(db=db, user_teacher_create=user_teacher_create)

    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    schedule_day_create = CreateScheduleDay(
        week_type=WeekType.UP,
        day=Days.MONDAY,
        time=Time.FIFTH
    )
    schedule_day = schedule_day_service.create_schedule_day(db=db, schedule_day_create=schedule_day_create)
    create_lesson = CreateLesson(
        discipline_id=discipline.id,
        user_teacher_id=user.id,
        group_id=group.id,
        schedule_day_id=schedule_day.id,
        subgroup=1,
        cabinet="416/2"
    )
    lesson = lesson_service.create_lesson(db=db, lesson_create=create_lesson)
    # When
    lessons = lesson_service.get_lessons_by_teacher_id(db=db, user_teacher_id=user.id)
    # Then
    assert len(lessons) == 1


def test_get_lessons_by_group_id_and_subgroup(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='ЭВМиПУ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    discipline = discipline_service.create_discipline(db=db, discipline_create=create_discipline)

    user_teacher_create = UserTeacherCreate(
        job_title="Ст.преподаватель",
        rank="Кандидат наук",
        email="prv59@bk.ru",
        name="Василий",
        surname="Прудников",
        second_name="Милайлович",
        password="12345678"
    )
    user = user_teacher_service.create_user_teacher(db=db, user_teacher_create=user_teacher_create)

    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    schedule_day_create = CreateScheduleDay(
        week_type=WeekType.UP,
        day=Days.MONDAY,
        time=Time.FIFTH
    )
    schedule_day = schedule_day_service.create_schedule_day(db=db, schedule_day_create=schedule_day_create)
    create_lesson = CreateLesson(
        discipline_id=discipline.id,
        user_teacher_id=user.id,
        group_id=group.id,
        schedule_day_id=schedule_day.id,
        subgroup=1,
        cabinet="416/2"
    )
    lesson = lesson_service.create_lesson(db=db, lesson_create=create_lesson)
    # When
    lessons = lesson_service.get_lessons_by_group_id_and_subgroup(db=db, group_id=group.id, subgroup=1)
    # Then
    assert len(lessons) == 1


def test_get_lessons_by_group_id(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='ЭВМиПУ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    discipline = discipline_service.create_discipline(db=db, discipline_create=create_discipline)

    user_teacher_create = UserTeacherCreate(
        job_title="Ст.преподаватель",
        rank="Кандидат наук",
        email="prv59@bk.ru",
        name="Василий",
        surname="Прудников",
        second_name="Милайлович",
        password="12345678"
    )
    user = user_teacher_service.create_user_teacher(db=db, user_teacher_create=user_teacher_create)

    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    schedule_day_create = CreateScheduleDay(
        week_type=WeekType.UP,
        day=Days.MONDAY,
        time=Time.FIFTH
    )
    schedule_day = schedule_day_service.create_schedule_day(db=db, schedule_day_create=schedule_day_create)
    create_lesson = CreateLesson(
        discipline_id=discipline.id,
        user_teacher_id=user.id,
        group_id=group.id,
        schedule_day_id=schedule_day.id,
        subgroup=1,
        cabinet="416/2"
    )
    lesson = lesson_service.create_lesson(db=db, lesson_create=create_lesson)
    # When
    lessons = lesson_service.get_lessons_by_group_id(db=db, group_id=group.id)
    # Then
    assert len(lessons) == 1

def test_get_lessons_by_user_teacher_id_and_schedule_day(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='ЭВМиПУ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    discipline = discipline_service.create_discipline(db=db, discipline_create=create_discipline)

    user_teacher_create = UserTeacherCreate(
        job_title="Ст.преподаватель",
        rank="Кандидат наук",
        email="prv59@bk.ru",
        name="Василий",
        surname="Прудников",
        second_name="Милайлович",
        password="12345678"
    )
    user = user_teacher_service.create_user_teacher(db=db, user_teacher_create=user_teacher_create)

    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    schedule_day_create = CreateScheduleDay(
        week_type=WeekType.UP,
        day=Days.MONDAY,
        time=Time.FIFTH
    )
    schedule_day = schedule_day_service.create_schedule_day(db=db, schedule_day_create=schedule_day_create)
    create_lesson = CreateLesson(
        discipline_id=discipline.id,
        user_teacher_id=user.id,
        group_id=group.id,
        schedule_day_id=schedule_day.id,
        subgroup=1,
        cabinet="416/2"
    )
    lesson_create = lesson_service.create_lesson(db=db, lesson_create=create_lesson)
    # When
    lesson = lesson_service.get_lesson_by_user_teacher_id_and_schedule_day(db=db, user_teacher_id=user.id, schedule_day_id=schedule_day.id)
    # Then
    assert lesson.id == lesson_create.id
    assert lesson.discipline_id == lesson_create.discipline_id
    assert lesson.user_teacher_id == lesson_create.user_teacher_id
    assert lesson.group_id == lesson_create.group_id
    assert lesson.schedule_day_id == lesson_create.schedule_day_id
    assert lesson.subgroup == lesson_create.subgroup
    assert lesson.cabinet == lesson_create.cabinet


def test_create_lesson(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='ЭВМиПУ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    discipline = discipline_service.create_discipline(db=db, discipline_create=create_discipline)

    user_teacher_create = UserTeacherCreate(
        job_title="Ст.преподаватель",
        rank="Кандидат наук",
        email="prv59@bk.ru",
        name="Василий",
        surname="Прудников",
        second_name="Милайлович",
        password="12345678"
    )
    user = user_teacher_service.create_user_teacher(db=db, user_teacher_create=user_teacher_create)

    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    schedule_day_create = CreateScheduleDay(
        week_type=WeekType.UP,
        day=Days.MONDAY,
        time=Time.FIFTH
    )
    schedule_day = schedule_day_service.create_schedule_day(db=db, schedule_day_create=schedule_day_create)
    create_lesson = CreateLesson(
        discipline_id=discipline.id,
        user_teacher_id=user.id,
        group_id=group.id,
        schedule_day_id=schedule_day.id,
        subgroup=1,
        cabinet="416/2"
    )
    # When
    lesson = lesson_service.create_lesson(db=db, lesson_create=create_lesson)
    # Then
    assert lesson.discipline_id == create_lesson.discipline_id
    assert lesson.user_teacher_id == create_lesson.user_teacher_id
    assert lesson.group_id == create_lesson.group_id
    assert lesson.schedule_day_id == create_lesson.schedule_day_id
    assert lesson.subgroup == create_lesson.subgroup
    assert lesson.cabinet == create_lesson.cabinet


def test_delete_lesson(db: Session):
    # Given
    create_discipline = CreateDiscipline(
        discipline_name='ЭВМиПУ',
        count_of_hours='200',
        description='Крутой предмет'
    )
    discipline = discipline_service.create_discipline(db=db, discipline_create=create_discipline)

    user_teacher_create = UserTeacherCreate(
        job_title="Ст.преподаватель",
        rank="Кандидат наук",
        email="prv59@bk.ru",
        name="Василий",
        surname="Прудников",
        second_name="Милайлович",
        password="12345678"
    )
    user = user_teacher_service.create_user_teacher(db=db, user_teacher_create=user_teacher_create)

    create_group = CreateGroup(
        group_number=191,
        group_name="ПИР",
        count_of_subgroup=2
    )
    group = group_service.create_group(db=db, created_group=create_group)

    schedule_day_create = CreateScheduleDay(
        week_type=WeekType.UP,
        day=Days.MONDAY,
        time=Time.FIFTH
    )
    schedule_day = schedule_day_service.create_schedule_day(db=db, schedule_day_create=schedule_day_create)
    create_lesson = CreateLesson(
        discipline_id=discipline.id,
        user_teacher_id=user.id,
        group_id=group.id,
        schedule_day_id=schedule_day.id,
        subgroup=1,
        cabinet="416/2"
    )
    lesson_create = lesson_service.create_lesson(db=db, lesson_create=create_lesson)
    # When
    lesson_service.delete_lesson(db=db, lesson_id=lesson_create.id)
    lesson = lesson_service.get_lesson_by_id(db=db, lesson_id=lesson_create.id)
    # Then
    assert lesson is None
