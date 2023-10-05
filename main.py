# main.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Customer, Product, Sale

# Create a SQLite database (you can change this to another database if needed)
DATABASE_URL = "sqlite:///milk_sales.db"
engine = create_engine(DATABASE_URL)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Create a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# CLI Commands (to be implemented)
def add_customer(name):
    customer = Customer(name=name)
    session.add(customer)
    session.commit()
    print(f"Customer '{name}' added.")

def add_product(name):
    product = Product(name=name)
    session.add(product)
    session.commit()
    print(f"Product '{name}' added.")

def record_sale(customer_id, product_id, quantity, total_amount):
    sale = Sale(customer_id=customer_id, product_id=product_id, quantity=quantity, total_amount=total_amount)
    session.add(sale)
    session.commit()
    print("Sale recorded.")

def list_customers():
    customers = session.query(Customer).all()
    for customer in customers:
        print(f"Customer ID: {customer.id}, Name: {customer.name}")

def list_products():
    products = session.query(Product).all()
    for product in products:
        print(f"Product ID: {product.id}, Name: {product.name}")

# Example CLI commands (to be expanded)
if __name__ == "__main__":
    while True:
        print("\nMilk Sales Reporting CLI")
        print("1. Add Customer")
        print("2. Add Product")
        print("3. Record Sale")
        print("4. List Customers")
        print("5. List Products")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            add_customer(name)
        elif choice == "2":
            name = input("Enter product name: ")
            add_product(name)
        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity sold: "))
            total_amount = float(input("Enter total amount: "))
            record_sale(customer_id, product_id, quantity, total_amount)
        elif choice == "4":
            list_customers()
        elif choice == "5":
            list_products()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

# models.py
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
