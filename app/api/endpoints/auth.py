from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.depends import get_db
from app.config.security import validate_password
from app.schemas import user
from app.service import user_service as user_service, user_teacher_service, user_student_service
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/sing-up-teacher", response_model=user.UserTeacher)
def create_teacher_user(user: user.UserTeacherCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_teacher_service.create_user_teacher(db=db, user_teacher_create=user)


@router.post("/sing-up-student", response_model=user.UserStudent)
def create_student_user(user: user.UserStudentCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_student_service.create_user_student(db=db, user_student_create=user)


@router.post("/auth", response_model=user.TokenBase)
def auth(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_service.get_user_by_email(db=db, email=form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    if not validate_password(password=form_data.password, hashed_password=user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    return user_service.create_user_token(db=db, user_id=user.id)
