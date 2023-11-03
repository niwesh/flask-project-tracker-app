import os

DEBUG = False
SECRET_KEY = 'topsecret'
# USERNAME = 'postgres' PASSWORD = 'Hello' DB_NAME = 'project_expense_tracker_db' SQLALCHEMY_DATABASE_URI =
# f'postgresql://{USERNAME}:{PASSWORD}@localhost/{DB_NAME}' SQLALCHEMY_DATABASE_URI =
# 'postgresql://nivesh_pg_user:Qqco25PDORSeKqUgSLviTnasTHNIaYU6@dpg-cl2k9c0310os73dhck5g-a.oregon-postgres.render.com
# /nivesh_pg'
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
