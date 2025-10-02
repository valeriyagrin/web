from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class User(BaseModel):
    id: int = Field(..., ge=1)
    email: EmailStr
    login: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=5, max_length=50)
    createdAt: datetime = None
    updatedAt: datetime = None
