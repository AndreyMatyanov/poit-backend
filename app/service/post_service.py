from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate


def get_post_list(db: Session):
    return db.query(Post).all()


def create_post(db: Session, item: PostCreate):
    post = Post(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
