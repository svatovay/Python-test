from typing import List

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from sql_app import crud, database, schemas

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}, )


# Изменённый /users-list/
@router.get("/", summary='Get Users', response_model=List[schemas.UserModel])
def read_users(q: List[int] = Query([0, 0], description='Возрастной диапазон пользователей'),
               db: Session = Depends(database.get_db)):
    """
    Получение списка пользователей
    Фильтрация по q - возрастному диапазону [min, max]
    """
    db_users = crud.get_users(db, age_range=q)
    return db_users


# Новый endpoint
@router.get("/{user_id}", response_model=schemas.UserModel)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    """
    Получение пользователя
    """
    db_user = crud.get_user(db, user_id=user_id)
    return db_user


# Изменённый /register-user/
@router.post("/", summary='Create User', response_model=schemas.UserModel)
def add_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """
    Добавление пользователя
    """
    db_user = crud.create_user(db, user=user)
    return db_user
