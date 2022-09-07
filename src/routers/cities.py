from fastapi import APIRouter, Query, HTTPException

from external_requests import CheckCityExisting
from sql_app.models import Session, City

router = APIRouter(
    prefix="/cities",
    tags=["cities"],
    responses={404: {"description": "Not found"}}, )


@router.get("/", summary='Get Cities')
def read_cities(q: str = Query(description="Название города", default=None)):
    """
    Получение списка городов
    Фильтрация по q - названию города
    """
    if q:
        return Session().query(City).filter(City.name == q).all()
    cities = Session().query(City).all()

    return [{'id': city.id, 'name': city.name, 'weather': city.weather} for city in cities]


@router.post("/{city}", summary='Create City')
def add_city(city: str = Query(description="Название города", default=None)):
    """
    Добавление города
    """
    if city is None:
        raise HTTPException(status_code=400, detail='Параметр city должен быть указан')
    check = CheckCityExisting()
    if not check.check_existing(city):
        raise HTTPException(status_code=400, detail='Параметр city должен быть существующим городом')

    city_object = Session().query(City).filter(City.name == city.capitalize()).first()
    if city_object is None:
        city_object = City(name=city.capitalize())
        s = Session()
        s.add(city_object)
        s.commit()

    return {'id': city_object.id, 'name': city_object.name, 'weather': city_object.weather}
