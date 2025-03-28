# Necessary imports
import os
from flask import Flask
from flask_session import Session
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import timedelta, datetime
from .routes import main_bp

# Function to initialize application 
def create_app():
    # Initialize application
    app = Flask(__name__)

    # Initialize environment variable
    app.secret_key = os.getenv('APP_SECRET_KEY')

    # Database Configuration (PostgreSQL on Heroku)
    DATABASE_URL = os.getenv('DATABASE_URL') #Use environment variable in production.
    engine = create_engine(DATABASE_URL)
    Base = declarative_base()

    class SessionTable(Base):
        __tablename__ = 'sessions'
        id = Column(Integer, primary_key=True)
        session_id = Column(String(255), unique=True)
        data = Column(String)
        expiry = Column(DateTime)

    Base.metadata.create_all(engine) #Create the table if it does not exist.

    # Flask-Session Configuration
    app.config["SESSION_TYPE"] = "sqlalchemy"
    app.config["SESSION_SQLALCHEMY"] = engine
    app.config["SESSION_SQLALCHEMY_TABLE"] = 'sessions' #Important to set the table name.
    app.config["SESSION_PERMANENT"] = True  # Sessions are permanent
    app.config["SESSION_USE_SIGNER"] = True #Securely sign cookies.
    app.config["SESSION_PERMANENT_SESSION_LIFETIME"] = timedelta(days=7) #Set the session timeout.
    


    Session(app)

    # Load configuration for application
    # app.config.from_object('config.Config')

    # Register blueprints and initialize routes
    #app.register_blueprint(main_bp)

    # Return application
    return app