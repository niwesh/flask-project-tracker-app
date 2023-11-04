# from sqlalchemy import create_engine, text
#
# database_uri = 'postgresql+psycopg2://nivesh_pg_user:Qqco25PDORSeKqUgSLviTnasTHNIaYU6@dpg-cl2k9c0310os73dhck5g-a.oregon-postgres.render.com/nivesh_pg'
#
# engine = create_engine(database_uri)
#
# connection = engine.connect()
#
# from sqlalchemy.exc import SQLAlchemyError
#
# try:
#     # Delete the row from the "project" table where id = 2
#     delete_query = text("DELETE FROM project WHERE id = 2")
#     connection.execute(delete_query)
# except SQLAlchemyError as e:
#     print("An error occurred while executing the DELETE query:", str(e))
#
# # Rest of your code for selecting and printing
#
#
# # Select everything from the "project" table
# query = text("SELECT * FROM project;")
# result = connection.execute(query)
#
# # Get the column names from cursor.description
# column_names = [column[0] for column in result.cursor.description]
#
# # Print the column names
# print(column_names)
#
# # Fetch and print the results
# for row in result.fetchall():
#     print(row)
#
# connection.close()

# import os
#
# DEBUG = False
# SECRET_KEY = 'topsecret'
# SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
# SQLALCHEMY_TRACK_MODIFICATIONS = False
