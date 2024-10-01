import os
import logging
from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify, flash
# from .utils.db import insert_user_response
# from .utils.questions import questions, post_survey_questions, final_survey_questions
# from .utils.demographics import demographics_questions
# from dotenv import load_dotenv, find_dotenv
# from openai import OpenAI

main_bp = Blueprint('main', __name__)

# Load .env variables
# load_dotenv(find_dotenv())

# Set variables
# client = OpenAI(api_key=os.getenv('API_KEY'))

# Set up logging
# logging.basicConfig(level=logging.DEBUG)

@main_bp.route('/')
def home():
    return "Overreliance Testing Platform (Flask Heroku App) Version -- 0.3.0"

# @main_bp.route('/')
# def index():
    # session.clear()
    # session['question_index'] = 0
    # session['answers'] = []
    # session['post_survey_answers'] = []
    # session['final_survey_answers'] = []
    # session['chat_history'] = []
    # session['user'] = []
    # session['user_id'] = []
    # return render_template('index.html')
    # return "Overreliance Testing Platform (Flask Heroku App) Version -- 0.3.0"
