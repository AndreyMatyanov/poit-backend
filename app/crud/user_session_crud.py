from datetime import datetime
from typing import Optional, List
from uuid import UUID

from sqlalchemy import update
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.tokens import UserSession
from app.schemas.session import CreateUserSession, UpdateUserSession


class CRUDSession(CRUDBase[UserSession, CreateUserSession, UpdateUserSession]):

    def get_session_by_token(self, db: Session, token: UUID) -> Optional[UserSession]:
        session = db.query(self.model).filter(self.model.token == str(token)).one_or_none()
        return session

    def get_session_after_expiration_date(self, db: Session, user_id: UUID, expires: datetime) -> List[UserSession]:
        stmt = db.query(self.model) \
            .filter(self.model.user_id == user_id) \
            .filter(self.model.expires >= expires)
        user_sessions = db.execute(stmt).scalars().all()
        return user_sessions

    def revoke(self, db: Session, token: UUID) -> None:
        stmt = update(self.model).where(self.model.token == str(token)).values(expires=datetime.now())
        db.execute(stmt)
        db.commit()

    def get_session_by_user_id(self, db: Session, user_id: UUID) -> Optional[UserSession]:
        session = db.query(self.model).filter(self.model.user_id == user_id) \
            .order_by(self.model.created_at.desc()).first()
        return session


user_session_crud = CRUDSession(UserSession)
