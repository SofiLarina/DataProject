"""
Создайте модели базы данных работников it-компании
Таблица Работники содержит следующие столбцы: id,имя,стаж, должности
Таблица Должности содержит следующие столбцы: id, название, работники.
Напишите функции вывода всех должностей запрашиваемого работника,
всех работников по должности, всех работников определенной должности со стажем больше 5.
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///it_company.db')

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience = Column(Integer)
    position_id = Column(Integer, ForeignKey('positions.id'))
    position = relationship("Position", back_populates="employees")

class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship("Employee", back_populates="position")

Base.metadata.create_all(engine)


def get_employee_positions(employee_name):
    with Session(bind=engine, autoflush=True) as db:
        employee = db.query(Employee).filter_by(name=employee_name).first()
        if employee:
            return [position.name for position in employee.position]
        else:
            return "Сотрудник не найден"
        db.commit()

def get_employees_by_position(position_name):
    with Session(bind=engine, autoflush=True) as db:
        position = db.query(Position).filter_by(name=position_name).first()
        if position:
            return [employee.name for employee in position.employees]
        else:
            return "Должность не найдена"
        db.commit()

def get_employees_by_position_and_experience(position_name, experience_threshold):
    with Session(bind=engine, autoflush=True) as db:
        employees = db.query(Employee).join(Position).filter(Position.name == position_name, Employee.experience > experience_threshold).all()
        if employees:
            return [employee.name for employee in employees]
        else:
            return "Не найдено сотрудников с указанной должностью и опытом работы"
        db.commit()

add_employee('Иванов', 5, 'Developer')
add_employee('Петров', 3, 'Developer')
add_employee('Сидоров', 7, 'Manager')
add_employee('Иванов', 4, 'Manager')
add_employee('Петров', 6, 'Tester')
add_employee('Сидоров', 8, 'Tester')