from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.stage_graduation_project import StageGraduationProject
from app.schemas.graduation_project import CreateStageGraduationProject, UpdateStageGraduationProject


class CRUDStepGraduateProject(CRUDBase[StageGraduationProject, CreateStageGraduationProject, UpdateStageGraduationProject]):
    def get_stages_by_project_id(self, db: Session, project_id: int):
        db_stages = db.query(self.model).filter(self.model.graduation_project_id == project_id).all()
        return db_stages


step_graduation_project_crud = CRUDStepGraduateProject(StageGraduationProject)
