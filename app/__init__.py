from flask import Flask

from .config import Config
from .extensions import db



### Creates the Flask application
def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)

    db.init_app(app)

    # Registers the Customers Blueprint Route with the app
    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app