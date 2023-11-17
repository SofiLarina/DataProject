from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Session
from sqlalchemy import Table

engine = create_engine("sqlite:///shop.db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey("role.id"))
    orders = relationship("Order", back_populates="user")
    roles = relationship("Role", back_populates="users")

class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship("User", back_populates="role")

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("category.id"))
    orders = relationship("Order", secondary="order_product", back_populates="cart")
    category = relationship("Category", back_populates="products")

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("Product", back_populates="category")

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    total_price =Column(Float)
    user_id = Column(Integer, ForeignKey("user.id"))
    cart = relationship("Product", secondary="order_product", back_populates="orders")
    user = relationship("User", back_populates="orders")

order_product = Table("order_product", Base.metadata,
                      Column("order_id", Integer, ForeignKey("order.id"), primary_key=True),
                      Column("product_id", Integer, ForeignKey("product.id"), primary_key=True))

Base.metadata.create_all(bind=engine)

def Create_Role(name):
    with Session(bind=engine, autoflush=False) as db:
        role = Role(name=name)
        db.add(role)
        db.commit()

def Create_User(email, password, role_id):
    with Session(bind=engine, autoflush=False) as db:
        user = User(email=email, password=password, role_id=role_id)
        db.add(user)
        db.commit()

def Create_Category(name):
    with Session(bind=engine, autoflush=False) as db:
        category = Category(name=name)
        db.add(category)
        db.commit()

def Create_Product(name, quantity, price, category_id):
    with Session(bind=engine, autoflush=False) as db:
        product = Product(name=name, quantity=quantity, price=price, category_id=category_id)
        db.add(product)
        db.commit()

def Create_Order(date, total_price, user_id):
    with Session(bind=engine, autoflush=False) as db:
        order = Order(date=date, total_price=total_price, user_id=user_id)
        db.add(order)
        db.commit()


Create_Role("Admin")
Create_User("kaplan2006@yandex.ru", "12345", 1)
Create_Category("Electronics")
Create_Product("Laptop", 10, 999.99, 1)
Create_Order("17.11.2023", 999.99, 1)