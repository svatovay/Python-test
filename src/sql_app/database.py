from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import models

# Создание сессии
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@postgres:5432/testcrt'
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Подключение базы (с автоматической генерацией моделей)
Base = declarative_base()

# Создание таблиц по моделям
models.Base.metadata.create_all(bind=engine)


def get_db():
    """
    Создаёт сессию и закрывает её после окончания работы
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()
