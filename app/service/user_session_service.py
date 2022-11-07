from datetime import datetime
from typing import Optional
from uuid import UUID

from app.crud.user_session_crud import user_session_crud
from app.models.tokens import UserSession as UserSessionModel

from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.session import UserSession
from app.schemas.user import UserBase


def get_user_session(db: Session, user_token: UUID) -> Optional[UserSession]:
    user_session: Optional[UserSession] = user_session_crud.get_session_by_token(db=db, token=user_token)
    if user_session:
        user: User = user_session.user
        user_session.user = user
        user_session = UserSession.from_orm(user_session)

    return user_session
