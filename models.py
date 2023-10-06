
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    sales = relationship("Sale", back_populates="customer")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    sales = relationship("Sale", back_populates="product")

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)
    quantity = Column(Integer)
    total_amount = Column(Float)

    customer = relationship("Customer", back_populates="sales")
    product = relationship("Product", back_populates="sales")
