from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "Flash Heroku app."

if __name__ == '__main__':
    app.run

# def create_app():
#     app = Flask(__name__)

#     app.secret_key = 'griffin'
    
#     # Load configuration
#     # app.config.from_object('config.Config')

#     # Register blueprints
#     from .routes import main_bp
#     app.register_blueprint(main_bp)

#     return app