"""
Manage the app extensions here rather than creating
them in individual modules
"""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for SQLAlchmey models.
    Provides an explicitly defined declarative model
    """


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
