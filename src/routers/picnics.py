import datetime as dt
from typing import List

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from sql_app import crud, database, schemas

router = APIRouter(
    prefix="/picnics",
    tags=["picnics"],
    responses={404: {"description": "Not found"}}, )


@router.get("/", summary='Get Picnics', response_model=List[schemas.PicnicModelRegUsers])
def read_picnics(datetime: dt.datetime = Query(default=None, description='Время пикника (по умолчанию не задано)'),
                 past: bool = Query(default=True, description='Включая уже прошедшие пикники'),
                 db: Session = Depends(database.get_db)):
    """
    Список всех пикников
    Фильтрация по дате и завершённости
    """
    # TODO: Доделать ответ
    db_picnics = crud.get_picnics(db, picnic_date=datetime, past=past)
    return db_picnics


@router.post("/", summary='Create Picnic', response_model=schemas.PicnicModel)
def add_picnic(picnic: schemas.PicnicCreate = Depends(),
               db: Session = Depends(database.get_db)):
    """
    Добавление пикника
    """
    db_picnic = crud.create_picnic(db, picnic=picnic)
    return db_picnic


@router.post('/register', summary='Picnic Registration', response_model=schemas.PicnicRegistrationModel)
def register_to_picnic(picnic_reg: schemas.PicnicRegistration = Depends(),
                       db: Session = Depends(database.get_db)):
    """
    Регистрация пользователя на пикник
    """
    picnic_reg_model = crud.create_picnic_registration_record(db, picnic_reg=picnic_reg)

    return picnic_reg_model
