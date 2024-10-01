from flask import Flask
from .routes import main_bp

def create_app():
    app = Flask(__name__)

    # app.secret_key = 'griffin'
    
    # Load configuration
    # app.config.from_object('config.Config')

    # Register blueprints
    app.register_blueprint(main_bp)

    return app
