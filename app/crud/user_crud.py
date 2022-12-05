from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy import select, update, desc, asc, func

from app.crud.base import CRUDBase
from app.models.user_student import UserStudent
from app.models.user_teacher import UserTeacher
from app.models.users import User
from app.schemas.user import UserCreate, UserUpdate, RoleType


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_user_by_id(self, db: Session, user_id: int) -> UserTeacher | UserStudent:
        stmt = select(self.model).where(self.model.id == user_id)
        user: Optional[User] = db.execute(stmt).unique().scalar_one_or_none()
        return user

    def get_users_by_role(self, db: Session, role: RoleType) -> List[UserTeacher | UserStudent]:
        users = db.query(self.model).filter(self.model.role == role)
        return users.all()

user_crud = CRUDUser(User)
