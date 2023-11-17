"""
Создайте модели базы данных с отношением 1 ко многим.
Читатель содержит столбцы : id,имя, список книг
Книга содержит столбцы: id,Название, автор.
1 читатель может иметь много книг.
Напишите функцию вывода всех книг для вводимого с клавиатуры читателя.
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///books.db")

# создаем базовый класс для модели
class Base(DeclarativeBase):
    pass

class Reader(Base):
    __tablename__ = "Reader"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    list_of_books = relationship("Book", back_populates="user")


class Book(Base):
    __tablename__ = "Book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    reader_id = Column(Integer, ForeignKey("Reader.id"))
    user = relationship("Reader", back_populates="list_of_books")

Base.metadata.create_all(bind=engine)

with Session(bind=engine, autoflush=True) as db:
    reader1 = Reader(name="Иванов")
    db.add(reader1)
    reader2 = Reader(name="Петров")
    db.add(reader2)
    db.commit()

with Session(bind=engine, autoflush=True) as db:
    book1 = Book(title="Война и мир", author="Лев Толстой", reader_id=1)
    db.add(book1)
    book2 = Book(title="Преступление и наказание", author="Федор Достоевский", reader_id=1)
    book3 = Book(title="Мастер и Маргарита", author="Михаил Булгаков", reader_id=2)
    db.add(book3)
    db.commit()

def show_books():
    with Session(bind=engine, autoflush=False) as db:
        name_reader = input("Введите имя читателя: ")
        reader = db.query(Reader).filter(Reader.name == name_reader).first()

        if reader:
            print(f"Книги читателя {name_reader}:")
            for book in reader.list_of_books:
                print(book.title)

        else:
            print(f"Читатель с именем {name_reader} не найден")

show_books()