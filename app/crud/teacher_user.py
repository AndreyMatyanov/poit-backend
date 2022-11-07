from sqlalchemy.orm import with_polymorphic

from app.crud.base import CRUDBase
from app.models.user_teacher import UserTeacher
from app.models.users import User
from app.schemas.user import UserTeacherCreate, UserTeacherUpdate

tournament_br_model = with_polymorphic(User, [UserTeacher])


class CRUDUserTeacher(CRUDBase[tournament_br_model, UserTeacherCreate, UserTeacherUpdate]):
    pass


user_teacher_crud = CRUDUserTeacher(UserTeacher)
