from pydantic import BaseModel
from datetime import datetime
from .users import UserOut

class PostBase(BaseModel):
    title: str
    content:str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    content: str
    created_at: datetime
    author: UserOut #come from users schema

    class Config:
        from_attributes = True

