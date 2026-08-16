from flask import Flask

from .config import Config
from .extensions import db, migrate



### Creates the Flask application
def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)

    # Initialise extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so they are registered with db.metadata
    from . import models

    # Registers blueprints
    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app