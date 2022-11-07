from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.depends import get_db, verify_admin
from app.schemas.lesson import Lesson, CreateLesson
from app.service import lesson_service, group_service

router = APIRouter()


@router.get('/', response_model=List[Lesson])
def get_all_lessons(db: Session = Depends(get_db)):
    return lesson_service.get_all_lessons(db=db)


@router.get('/get-by-user-teacher-id/{user_teacher_id}', response_model=List[Lesson])
def get_lessons_by_user_teacher_id(user_teacher_id: int, db: Session = Depends(get_db)):
    return lesson_service.get_lessons_by_teacher_id(db=db, user_teacher_id=user_teacher_id)


@router.get('/get-lesson-for-students/{group_id}/', response_model=List[Lesson])
def get_lesson_by_group_id(group_id: int, db: Session = Depends(get_db)):
    return lesson_service.get_lessons_by_group_id(db=db, group_id=group_id)


@router.get('/get-lesson-for-students/{group_id}/{subgroup}', response_model=List[Lesson])
def get_lesson_by_group_id(group_id: int, subgroup: int, db: Session = Depends(get_db)):
    return lesson_service.get_lessons_by_group_id(db=db, group_id=group_id)


@router.post('/', response_model=Lesson)
def create_lesson(lesson_create: CreateLesson, db: Session = Depends(get_db), _=Depends(verify_admin)):
    group = group_service.get_group_by_id(db=db, group_id=lesson_create.group_id)
    lesson = lesson_service.get_lesson_by_user_teacher_id_and_schedule_day(
        db=db,
        user_teacher_id=lesson_create.user_teacher_id,
        schedule_day_id=lesson_create.schedule_day_id
    )
    if lesson:
        raise HTTPException(status_code=400, detail="Пара занята")
    if lesson_create.subgroup > group.count_of_subgroup:
        raise HTTPException(status_code=400, detail="Такой подгруппы не существует")
    return lesson_service.create_lesson(db=db, lesson_create=lesson_create)


@router.delete('/{lesson_id}', response_model=Lesson)
def delete_lesson(lesson_id: int, db: Session = Depends(get_db), _=Depends(verify_admin)):
    return lesson_service.delete_lesson(db=db, lesson_id=lesson_id)
