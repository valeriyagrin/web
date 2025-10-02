from pydantic import BaseModel, Field
from datetime import datetime

class Post(BaseModel):
    id: int = Field(..., ge=1)
    authorId: int = Field(..., ge=1)
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)
    createdAt: datetime = None
    updatedAt: datetime = None
