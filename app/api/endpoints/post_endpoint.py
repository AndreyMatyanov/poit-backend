from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..depends import get_db
from app.service import post_service as post_service
from ...schemas.post import PostCreate, PostList

router = APIRouter()


@router.get("/", response_model=List[PostList])
def post_list(db: Session = Depends(get_db)):
    return post_service.get_post_list(db)


@router.post("/")
def create_post(item: PostCreate, db: Session = Depends(get_db)):
    return post_service.create_post(db, item)
