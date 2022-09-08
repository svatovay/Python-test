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
    Возвращает модели пикников со списком зарегистрированных пользователей
    """
    if picnic_date is not None:
        db_picnics = db.query(models.Picnic).filter(models.Picnic.time == picnic_date).all()
    if not past:
        db_picnics = db.query(models.Picnic).filter(models.Picnic.time >= dt.datetime.now()).all()

    picnic_model_reg_users = [{
        'id': picnic.id,
        'city': db.query(models.City).filter(models.City.id == picnic.city_id).first(),
        'time': picnic.time,
        'users': [reg.user for reg in picnic.users]
    } for picnic in db_picnics]
    return picnic_model_reg_users


def create_picnic(db: Session, picnic: schemas.PicnicCreate):
    """
    Создает запись в БД с моделью города
    """
    db_picnic = models.Picnic(**picnic.dict())
    db.add(db_picnic)
    db.commit()
    db.refresh(db_picnic)
    return db_picnic


def create_picnic_registration_record(db: Session, picnic_reg: schemas.PicnicRegistration):
    """
    Делает регистрационную запись: пользователь -> пикник
    """
    db_picnic_reg = models.PicnicRegistration(**picnic_reg.dict())
    db.add(db_picnic_reg)
    db.commit()
    db.refresh(db_picnic_reg)
    picnic_reg_model = {
        'id': db_picnic_reg.id,
        'user': db_picnic_reg.user,
        'picnic_city': db.query(models.City).filter(models.City.id == db_picnic_reg.picnic.city_id).first(),
        'picnic_datetime': db_picnic_reg.picnic.time,
    }
    return picnic_reg_model
