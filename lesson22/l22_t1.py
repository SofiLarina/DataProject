"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

# создаем движок SqlAlchemy
engine = create_engine("sqlite:///films.db")

# создаем базовый класс для модели
class Base(DeclarativeBase):
    pass

# создаем модель БД(будем конвертировать в табличку)
class Films(Base):
    __tablename__ = "Фильмы"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    year = Column(Integer)
    genre = Column(String)
    rating = Column(Float)

# создаем таблицы
Base.metadata.create_all(bind=engine)

def create_film(name, year, genre, rating):
    with Session(bind=engine, autoflush=False) as db:
        new_film = Films(name=name, year=year, genre=genre, rating=rating)
        db.add(new_film)
        db.commit()

def show_films():
    with Session(bind=engine, autoflush=False) as db:
        all_films = db.query(Films).all()
        print(all_films)
        for film in all_films:
            print(film.name, "-", film.year, ":", film.rating)

def show_film_of_year(year):
    with Session(bind=engine, autoflush=False) as db:
        film = db.query(Films).filter(Films.year == year).first()
        print(film.name)

show_film_of_year(1997)
