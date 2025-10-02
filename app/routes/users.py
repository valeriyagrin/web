from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.models.user import User
import app.storage.db as db

router = APIRouter(prefix="/users", tags=["Users"])

# Получить всех пользователей
@router.get("/")
async def get_users():
    return db.users

# Создать пользователя
@router.post("/")
async def create_user(user: User):
    for u in db.users:
        if u["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")

    user.createdAt = datetime.now()
    user.updatedAt = datetime.now()

    db.users.append(user.dict())
    db.save_data()
    return user.dict()

# Получить пользователя по id
@router.get("/{user_id}")
async def get_user(user_id: int):
    for u in db.users:
        if u["id"] == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

# Обновить пользователя
@router.put("/{user_id}")
async def update_user(user_id: int, updated_user: User):
    for idx, u in enumerate(db.users):
        if u["id"] == user_id:
            updated_user.createdAt = u["createdAt"]
            updated_user.updatedAt = datetime.now()
            db.users[idx] = updated_user.dict()
            db.save_data()
            return updated_user.dict()
    raise HTTPException(status_code=404, detail="User not found")

# Удалить пользователя
@router.delete("/{user_id}")
async def delete_user(user_id: int):
    for u in db.users:
        if u["id"] == user_id:
            db.users.remove(u)
            db.save_data()
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
