from operator import or_

from app.crud.base import CRUDBase
from sqlalchemy.orm import Session
from app.models.lesson import Lesson
from app.schemas.lesson import CreateLesson, UpdateLesson


class CRUDLesson(CRUDBase[Lesson, CreateLesson, UpdateLesson]):
    def get_lessons_by_teacher_id(self, db: Session, user_teacher_id: int):
        lessons_db = db.query(self.model).filter(self.model.user_teacher_id == user_teacher_id).all()
        return lessons_db

    def get_lessons_by_group_id(self, db: Session, group_id: int):
        lesson_db = db.query(self.model).filter(self.model.group_id == group_id).all()
        return lesson_db

    def get_lessons_by_group_id_and_subgroup(self, db: Session, group_id: int, subgroup: int):
        lesson_db = db.query(self.model) \
            .filter(self.model.group_id == group_id) \
            .filter(or_(self.model.subgroup == 0, self.model.subgroup == subgroup)).all()
        return lesson_db

    def get_lesson_by_user_teacher_id_and_schedule_day(self, db: Session, user_teacher_id: int, schedule_day_id: int):
        lesson_db = db.query(self.model) \
            .filter(self.model.user_teacher_id == user_teacher_id) \
            .filter(self.model.schedule_day_id == schedule_day_id) \
            .one_or_none()
        return lesson_db


lesson_crud = CRUDLesson(Lesson)
