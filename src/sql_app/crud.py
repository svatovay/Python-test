import datetime as dt

from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    """
    Возвращает модель пользователя из БД
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, age_range: list):
    """
    Возвращает модели пользователя из БД
    """
    if age_range[0] or age_range[1]:
        return db.query(models.User).filter(models.User.age.between(*age_range)).all()
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    """
    Создает запись в БД с моделью пользователя
    """
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_city(db: Session, name: str):
    """
    Возвращает модель города из БД
    """
    return db.query(models.City).filter(models.City.name == name).first()


def get_cities(db: Session):
    """
    Возвращает модели городов из БД
    """
    return db.query(models.City).all()


def create_city(db: Session, city: schemas.CityCreate):
    """
    Создает запись в БД с моделью города
    """
    db_city = models.City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def get_picnic(db: Session, name: str):
    """
    Возвращает модель пикника из БД
    """
    return db.query(models.City).filter(models.City.name == name).first()


def get_picnics(db: Session, picnic_date: dt.datetime, past: bool = True):
    """
    Возвращает модели пикников из БД
    """
    # TODO: Возможно формировать итоговый ответ для запроса
    if picnic_date is not None:
        db_picnics = db.query(models.Picnic).filter(models.Picnic.time == picnic_date)
    if not past:
        db_picnics = db.query(models.Picnic).filter(models.Picnic.time >= dt.datetime.now())

    return db_picnics


def create_picnic(db: Session, picnic: schemas.PicnicCreate):
    """
    Создает запись в БД с моделью города
    """
    db_picnic = models.Picnic(**picnic.dict())
    db.add(db_picnic)
    db.commit()
    db.refresh(db_picnic)
    return db_picnic


def create_picnic_registration_record(db: Session, city: schemas.CityCreate):
    """
    Делает регистрационную запись: пользователь -> пикник
    """
    db_city = models.City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city
