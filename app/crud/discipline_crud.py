from app.crud.base import CRUDBase
from app.models.discipline import Discipline
from app.schemas.lesson import CreateDiscipline, UpdateDiscipline


class CRUDDiscipline(CRUDBase[Discipline, CreateDiscipline, UpdateDiscipline]):
    pass


discipline_crud = CRUDDiscipline(Discipline)
