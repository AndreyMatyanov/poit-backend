from app.crud.base import CRUDBase
from app.models.course_project_user_teacher import CourseProjectUserTeacher
from app.schemas.course_project import CreateCourseProjectUserTeacher, UpdateCourseProjectUserTeacher


class CRUDCourseProjectUserTeacher(CRUDBase[CourseProjectUserTeacher, CreateCourseProjectUserTeacher, UpdateCourseProjectUserTeacher]):
    pass


course_project_user_teacher_crud = CRUDCourseProjectUserTeacher(CourseProjectUserTeacher)
