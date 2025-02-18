from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class PostBase(BaseModel):
    id: Optional[int] = None
    content: str
    title: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class CreatePost(PostBase):
    pass