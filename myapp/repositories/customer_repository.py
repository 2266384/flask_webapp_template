from myapp.models import Customer


def find_customers_by_postcode(postcode):
    return (
        db.session.query(Customer)
        .filter(Customer.postcode == postcode)
        .all()
    )