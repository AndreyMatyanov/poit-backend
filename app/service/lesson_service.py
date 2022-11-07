from typing import List, Optional
from pydantic import parse_obj_as

from sqlalchemy.orm import Session

from app.crud.group_crud import group_crud
from app.crud.lesson_crud import lesson_crud
from app.schemas.lesson import Lesson, CreateLesson
from app.service import group_service


def get_all_lessons(db: Session) -> List[Lesson]:
    lessons_db = lesson_crud.get_multi(db=db)
    return [Lesson.from_orm(lesson) for lesson in lessons_db]


def get_lesson_by_id(db: Session, lesson_id: int) -> Optional[Lesson]:
    lesson_db = lesson_crud.get(db=db, id=lesson_id)
    if lesson_db is None:
        return None
    return parse_obj_as(Lesson, lesson_db)


def get_lessons_by_teacher_id(db: Session, user_teacher_id: int) -> List[Lesson]:
    lessons_db = lesson_crud.get_lessons_by_teacher_id(db=db, user_teacher_id=user_teacher_id)
    return [Lesson.from_orm(lesson) for lesson in lessons_db]


def get_lessons_by_group_id(db: Session, group_id: int) -> List[Lesson]:
    lessons_db = lesson_crud.get_lessons_by_group_id(db=db, group_id=group_id)
    return [Lesson.from_orm(lesson) for lesson in lessons_db]


def get_lessons_by_group_id_and_subgroup(db: Session, group_id: int, subgroup: int) -> List[Lesson]:
    lessons_db = lesson_crud.get_lessons_by_group_id_and_subgroup(db=db, group_id=group_id, subgroup=subgroup)
    return [Lesson.from_orm(lesson) for lesson in lessons_db]


def get_lesson_by_user_teacher_id_and_schedule_day(
        db: Session,
        user_teacher_id: int,
        schedule_day_id: int
) -> Optional[Lesson]:
    lesson_db = lesson_crud.get_lesson_by_user_teacher_id_and_schedule_day(
        db=db,
        user_teacher_id=user_teacher_id,
        schedule_day_id=schedule_day_id
    )
    return parse_obj_as(Lesson, lesson_db)


def create_lesson(db: Session, lesson_create: CreateLesson) -> Lesson:
    lesson_db = lesson_crud.create(db=db, obj_in=lesson_create)
    return parse_obj_as(Lesson, lesson_db)


def delete_lesson(db: Session, lesson_id: int) -> Lesson:
    lesson_db = lesson_crud.remove(db=db, id=lesson_id)
    return True  # ИСПРАВИТЬ
