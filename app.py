from flask import Flask

# from app import app
from app import create_app

# app = app
app = create_app()

if __name__ == "__main__":
    app.run()
