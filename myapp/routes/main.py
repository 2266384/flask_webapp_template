import logging
from datetime import datetime

from flask import Blueprint, render_template
from sqlalchemy import text

from myapp.extensions import db


logger = logging.getLogger(__name__)

main_bp = Blueprint("main", __name__)



# Test the database connection
@main_bp.get("/")
def index():
    database_connected = False
    database_error = None

    try:
        db.session.execute(text("SELECT 1"))
        database_connected = True

    except Exception as exc:
        db.session.rollback()
        logger.exception("Database connection failed")
        database_error = str(exc)

    return render_template(
        "index.html",
        database_connected=database_connected,
        database_error=database_error,
        current_year=datetime.now().year,
    )