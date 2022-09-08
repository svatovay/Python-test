import datetime as dt
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Родительская модель пользователя
    """
    name: str
    surname: str
    age: int


class UserCreate(UserBase):
    """
    Модель для создания пользователя
    """
    pass


class UserModel(UserBase):
    """
    Модель пользователя для вывода
    """
    id: int

    class Config:
        orm_mode = True


class CityBase(BaseModel):
    """
    Родительская модель города
    """
    name: str


class CityCreate(CityBase):
    """
    Модель для создания города
    """
    pass


class CityModel(CityBase):
    """
    Модель города для вывода
    """
    id: int
    weather: str

    class Config:
        orm_mode = True


class PicnicBase(BaseModel):
    """
    Родительская модель пикника
    """
    city_id: int
    time: dt.datetime


class PicnicCreate(PicnicBase):
    """
    Модель для создания пикника
    """
    pass


class PicnicModel(PicnicBase):
    """
    Модель пикника для вывода
    """
    id: int

    class Config:
        orm_mode = True


class PicnicModelRegUsers(BaseModel):
    """
    Модель для вывода пикника со списком зарегистрированных пользователей
    """
    id: int
    city: CityModel
    time: dt.datetime
    users: List[UserModel]

    class Config:
        orm_mode = True


class PicnicRegistration(BaseModel):
    """
    Модель для создания регистрационной записи пользователя на пикник
    """
    user_id: int
    picnic_id: int


class PicnicRegistrationModel(BaseModel):
    """
    Модель для вывода регистрационной записи пользователя на пикник
    """
    id: int
    user: UserModel
    picnic_city: CityModel
    picnic_datetime: dt.datetime
