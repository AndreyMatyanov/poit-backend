from app.crud.base import CRUDBase
from app.models.stage_course_project import StageCourseProject
from app.schemas.course_project import CreateStageCourseProject, UpdateStageCourseProject


class CRUDStepCourseProject(CRUDBase[StageCourseProject, CreateStageCourseProject, UpdateStageCourseProject]):
    pass


step_course_project_crud = CRUDStepCourseProject(StageCourseProject)
