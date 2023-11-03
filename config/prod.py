import os

DEBUG = False
SECRET_KEY = 'topsecret'
USERNAME = 'postgres'
PASSWORD = 'Hello'
DB_NAME = 'project_expense_tracker_db'
SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@localhost/{DB_NAME}'
# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
