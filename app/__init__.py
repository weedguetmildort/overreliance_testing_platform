from flask import Flask
from .routes import main_bp

app = Flask(__name__)

@app.route('/')
def index():
    return "Overreliance Testing Platform (Flask Heroku App) Version -- 0.2.1"

# def create_app():
#     app = Flask(__name__)

    # app.secret_key = 'griffin'
    
    # Load configuration
    # app.config.from_object('config.Config')

    # Register blueprints
    # app.register_blueprint(main_bp)
    # @app.route('/')
    # def index():
    #     return "Overreliance Testing Platform (Flask Heroku App) Version -- 0.3.0"

    # return app
