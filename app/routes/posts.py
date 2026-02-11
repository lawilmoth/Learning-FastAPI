from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .users import get_db
from app.schemas.post import PostCreate, Post
from app.crud.posts import create_post, get_posts_for_user, get_all_posts
from app.auth.sessions import get_current_user

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=Post)
def create_new_post(
    post: PostCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_post(db, user_id, post)

@router.get("/", response_model=list[Post])
def get_my_posts(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_all_posts(db)
