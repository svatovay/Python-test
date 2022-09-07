import datetime as dt

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from sql_app import crud, database, schemas

router = APIRouter(
    prefix="/picnics",
    tags=["picnics"],
    responses={404: {"description": "Not found"}}, )


@router.get("/", summary='Get Picnics')
def read_picnics(datetime: dt.datetime = Query(default=None, description='Время пикника (по умолчанию не задано)'),
                 past: bool = Query(default=True, description='Включая уже прошедшие пикники'),
                 db: Session = Depends(database.get_db)):
    """
    Список всех пикников
    Фильтрация по дате и завершённости
    """
    # TODO: Доделать ответ
    db_picnics = crud.get_picnics(db, picnic_date=datetime, past=past)
    return [schemas.PicnicModel.from_orm(db_picnic) for db_picnic in db_picnics]

    # return [{
    #     'id': pic.id,
    #     'city': Session().query(City).filter(City.id == pic.id).first().name,
    #     'time': pic.time,
    #     'users': [
    #         {
    #             'id': pr.user.id,
    #             'name': pr.user.name,
    #             'surname': pr.user.surname,
    #             'age': pr.user.age,
    #         }
    #         for pr in Session().query(PicnicRegistration).filter(PicnicRegistration.picnic_id == pic.id)],
    # } for pic in picnics]


@router.post("/", summary='Create Picnic')
def add_picnic(picnic: schemas.PicnicCreate = Depends(),
               db: Session = Depends(database.get_db)):
    """
    Добавление пикника
    """
    db_picnic = crud.create_picnic(db, picnic=picnic)
    return schemas.PicnicModel.from_orm(db_picnic)

# @router.post('/register/', summary='Picnic Registration')
# def register_to_picnic(user_id: int = None, picnic_id: int = None, ):
#     """
#     Регистрация пользователя на пикник
#     """
        # TODO: Сделать запрос
#     pr = PicnicRegistration(user_id=user_id, picnic_id=picnic_id)
#     s = Session()
#     s.add(pr)
#     s.commit()
#
#     return {
#         'id': pr.id,
#         'user': Session().query(User).filter(User.id == pr.user_id).first().name,
#         'picnic_city': Session().query(City).filter(
#             City.id == Session().query(Picnic).filter(
#                 Picnic.id == pr.picnic_id).first().city_id).first().name,
#         'picnic_datetime': Session().query(Picnic).filter(Picnic.id == pr.picnic_id).first().time,
#     }
