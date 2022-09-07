from typing import List

from fastapi import APIRouter, Query

from sql_app.models import Session, User
from sql_app.schemas import RegisterUserRequest, UserModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}, )


@router.get("/", summary='Get Users')
def read_users(q: List[int] = Query([1, 150], description='Возрастной диапазон пользователей')):
    """
    Список пользователей
    Фильтрация по q - возрастному диапазону [min, max]
    """

    if q:
        return Session().query(User).filter(User.age.between(q[0], q[1])).all()

    users = Session().query(User).all()
    return [{
        'id': user.id,
        'name': user.name,
        'surname': user.surname,
        'age': user.age,
    } for user in users]


# @router.get("/{pk}")
# def read_user(user: UserModel):
#     """
#     Получение пользователя
#     """
#     return UserModel.from_orm(user_object)


@router.post("/{username}", summary='Create User')
def add_user(user: RegisterUserRequest):
    """
    Добавление пользователя
    """
    user_object = User(**user.dict())
    s = Session()
    s.add(user_object)
    s.commit()

    return UserModel.from_orm(user_object)
