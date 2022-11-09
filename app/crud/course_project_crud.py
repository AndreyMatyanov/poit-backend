from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.course_project_base import CourseProjectBase
from app.schemas.course_project import CreateCourseProject, UpdateCourseProject


class CRUDCourseProject(CRUDBase[CourseProjectBase, CreateCourseProject, UpdateCourseProject]):
    def get_projects_by_user_student_id(self, db: Session, user_student_id: int):
        course_project_db = db.query(self.model).filter(self.model.user_student_id == user_student_id).all()
        return course_project_db


course_project_crud = CRUDCourseProject(CourseProjectBase)
