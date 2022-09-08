from typing import List

from fastapi import APIRouter, Query, HTTPException, Depends
from sqlalchemy.orm import Session

from external_requests import CheckCityExisting
from sql_app import crud, database, schemas

router = APIRouter(
    prefix="/cities",
    tags=["cities"],
    responses={404: {"description": "Not found"}}, )


# Замена /get-cities/
@router.get("/", summary='Get Cities', response_model=List[schemas.CityModel])
def read_cities(db: Session = Depends(database.get_db)):
    """
    Получение списка городов
    """
    db_cities = crud.get_cities(db)
    return db_cities


# Изменённый /get-cities/ c q
@router.get("/{city_name}", summary='Get City', response_model=schemas.CityModel)
def read_city(q: str = Query(description="Название города", default=None),
              db: Session = Depends(database.get_db)):
    """
    Получение города по q - названию города
    """
    db_city = crud.get_city(db, name=q)
    return db_city


# Изменённый /create-city/
@router.post("/", summary='Create City', response_model=schemas.CityModel)
def add_city(city: schemas.CityCreate,
             db: Session = Depends(database.get_db)):
    """
    Добавление города
    """
    if city.name is None:
        raise HTTPException(status_code=400, detail='Параметр city должен быть указан')
    check = CheckCityExisting()
    if not check.check_existing(city.name):
        raise HTTPException(status_code=400, detail='Параметр city должен быть существующим городом')

    db_city = crud.get_city(db, name=city.name)
    if db_city is None:
        db_city = crud.create_city(db, city)

    return db_city
