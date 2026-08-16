'''
    Manage the app extensions here rather than creating
    them in individual modules
'''

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


migrate = Migrate()
db = SQLAlchemy()