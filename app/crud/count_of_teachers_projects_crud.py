from app.crud.base import CRUDBase
from app.models.count_of_teachers_projects import CountOfTeachersProjects
from app.schemas.count_of_teachers_project import CreateCountOfTeacherProject, UpdateCountOfTeacherProject


class CRUDCountOfTeachersProjects(CRUDBase[CountOfTeachersProjects, CreateCountOfTeacherProject, UpdateCountOfTeacherProject]):
    pass


course_project_user_teacher_crud = CRUDCountOfTeachersProjects(CountOfTeachersProjects)