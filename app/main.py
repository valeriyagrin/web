from fastapi import FastAPI
from app.routes import users, posts
from app.storage import db

app = FastAPI(title="Blog API")

# Загружаем данные при запуске
@app.on_event("startup")
async def startup_event():
    db.load_data()

# Сохраняем данные при остановке
@app.on_event("shutdown")
async def shutdown_event():
    db.save_data()

app.include_router(users.router)
app.include_router(posts.router)

@app.get("/")
async def root():
    return {"message": "Hello, Blog API is running!"}
