from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.models.post import Post
import app.storage.db as db

router = APIRouter(prefix="/posts", tags=["Posts"])

# Получить все посты
@router.get("/")
async def get_posts():
    return db.posts

# Создать пост
@router.post("/")
async def create_post(post: Post):
    author_exists = any(u["id"] == post.authorId for u in db.users)
    if not author_exists:
        raise HTTPException(status_code=400, detail="Author not found")

    post.createdAt = datetime.now()
    post.updatedAt = datetime.now()

    db.posts.append(post.dict())
    db.save_data()
    return post.dict()

# Получить пост по id
@router.get("/{post_id}")
async def get_post(post_id: int):
    for p in db.posts:
        if p["id"] == post_id:
            return p
    raise HTTPException(status_code=404, detail="Post not found")

# Обновить пост
@router.put("/{post_id}")
async def update_post(post_id: int, updated_post: Post):
    for idx, p in enumerate(db.posts):
        if p["id"] == post_id:
            updated_post.createdAt = p["createdAt"]
            updated_post.updatedAt = datetime.now()
            db.posts[idx] = updated_post.dict()
            db.save_data()
            return updated_post.dict()
    raise HTTPException(status_code=404, detail="Post not found")

# Удалить пост
@router.delete("/{post_id}")
async def delete_post(post_id: int):
    for p in db.posts:
        if p["id"] == post_id:
            db.posts.remove(p)
            db.save_data()
            return {"message": "Post deleted"}
    raise HTTPException(status_code=404, detail="Post not found")
