from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostBase(BaseModel):
    id: Optional[int] = None
    content: str
    title: str
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class CreatePost(PostBase):
    class Config:
        orm_mode = True