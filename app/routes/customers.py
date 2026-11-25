from flask import Blueprint, jsonify
from flask.typing import ResponseReturnValue

from app.services import get_customer

customers_bp = Blueprint("customers", __name__, url_prefix="/customers")


@customers_bp.get("/<int:customer_id>")
def customer(customer_id: int) -> ResponseReturnValue:
    customer = get_customer(customer_id)

    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify({"id": customer.id, "name": customer.name})
