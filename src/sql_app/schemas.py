import datetime as dt

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str
    age: int


class UserCreate(UserBase):
    pass


class UserModel(UserBase):
    id: int

    class Config:
        orm_mode = True


class CityBase(BaseModel):
    name: str


class CityCreate(CityBase):
    pass


class CityModel(CityBase):
    id: int
    weather: str

    class Config:
        orm_mode = True


class PicnicBase(BaseModel):
    city_id: int
    time: dt.datetime


class PicnicCreate(PicnicBase):
    pass


class PicnicModel(PicnicBase):
    id: int

    class Config:
        orm_mode = True


class PicnicRegistration(BaseModel):
    id: int
    user_id: int
    picnic_id: int
