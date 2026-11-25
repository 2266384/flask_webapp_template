from sqlalchemy import select

from app.extensions import db
from app.models import Customer


def find_customers_by_email(email: str) -> list[Customer]:
    """Find customers matching an email address."""

    statement = select(Customer).where(Customer.email == email)

    return list(db.session.scalars(statement).all())
