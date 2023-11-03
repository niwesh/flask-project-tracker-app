import os

DEBUG = False
SECRET_KEY = 'topsecret'
# USERNAME = 'postgres'
# PASSWORD = 'Hello'
# DB_NAME = 'project_expense_tracker_db'
# SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@localhost/{DB_NAME}'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://zcnggeemiexrzr:ffe773479ecb0f5ccb0e648ff7214a134e9cfc6dc4c591d976379107f44b9c4b@ec2-34-233-242-44.compute-1.amazonaws.com:5432/dad6etf2er56od'
SQLALCHEMY_TRACK_MODIFICATIONS = False
