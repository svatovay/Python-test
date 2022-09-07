from typing import List

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from sql_app import crud, database, schemas

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}, )


@router.get("/", summary='Get Users')
def read_users(q: List[int] = Query([0, 0], description='Возрастной диапазон пользователей'),
               db: Session = Depends(database.get_db)):
    """
    Получение списка пользователей
    Фильтрация по q - возрастному диапазону [min, max]
    """
    db_users = crud.get_users(db, age_range=q)
    return [schemas.UserModel.from_orm(db_user) for db_user in db_users]


@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    """
    Получение пользователя
    """
    db_user = crud.get_user(db, user_id=user_id)
    return schemas.UserModel.from_orm(db_user)


@router.post("/", summary='Create User')
def add_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """
    Добавление пользователя
    """
    db_user = crud.create_user(db, user=user)
    return schemas.UserModel.from_orm(db_user)
