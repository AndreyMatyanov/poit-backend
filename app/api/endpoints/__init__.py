from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..depends import get_db
from app.service import post_service
from ...schemas.post import PostCreate, PostList

router = APIRouter()


@router.get("/register", response_model=List[PostList])
def login(db: Session = Depends(get_db)):
    return post_service.get_post_list(db)


@router.post("/login")
def register(item: PostCreate, db: Session = Depends(get_db)):
    return post_service.create_post(db, item)
