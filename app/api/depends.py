import hashlib
from datetime import datetime
from typing import Optional
from uuid import UUID

from fastapi import Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
from passlib.handlers.bcrypt import bcrypt
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request
import random
import string

from app.db.database import SessionLocal
from app.models.tokens import UserSession as UserSessionModel
from app.models.users import User
from app.schemas.session import UserSession
from app.schemas.user import RoleType, UserBase
from app.service import user_service, user_session_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def exchange_token(x_auth_token: UUID = Header(...), db: Session = Depends(get_db)) -> UserSession:
    session: Optional[UserSession] = user_session_service.get_user_session(db, x_auth_token)

    if (not session) or (session.expires < datetime.now()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token not found or has expired')

    return session


def verify_admin(user_session: UserSession = Depends(exchange_token), db: Session = Depends(get_db)):
    user: UserBase = user_service.get_user_by_id(db=db, id=user_session.user_id)

    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Permission dined")

    return user


def verify_teacher(user_session: UserSession = Depends(exchange_token), db: Session = Depends(get_db)):
    user: UserBase = user_service.get_user_by_id(db=db, id=user_session.user_id)

    if user.role != RoleType.TEACHER:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Permission dined")

    return user
