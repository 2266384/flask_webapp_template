from sqlalchemy import select

from app.extensions import db
from app.models import Customer


def get_customer(customer_id: int) -> Customer | None:
    """Retrieve a customer by ID"""
    statement = select(Customer).where(Customer.id == customer_id)
    return db.session.scalar(statement)


def create_customer(name: str, email: str) -> Customer:
    """Create and persist a new customer"""
    customer = Customer(name=name, email=email)

    db.session.add(customer)
    db.session.commit()

    return customer
