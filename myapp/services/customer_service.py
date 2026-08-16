from myapp.models import Customer
from myapp.extensions import db

def get_customer(customer_id):
    return db.session.get(Customer, customer_id)


def create_customer(name, email):
    customer = Customer(
        name=name,
        email=email
    )

    db.session.add(customer)
    db.session.commit()

    return customer