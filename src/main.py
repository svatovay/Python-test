from fastapi import FastAPI
from routers import users, cities, picnics
from sql_app import models, database

# Создание таблиц по моделям
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Подключение роуетров и эндпоинтов
app.include_router(users.router)
app.include_router(cities.router)
app.include_router(picnics.router)


@app.get("/")
def root():
    return {"message": "Picnic WebApp"}
