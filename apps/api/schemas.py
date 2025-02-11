from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    id: Optional[int] = None
    content: str
    title: str

    class Config:
        orm_mode = True


class CreatePost(PostBase):
    class Config:
        orm_mode = True