import os

from app import create_app, db  # from the app package __init__

# if __name__ == '__main__':
#     flask_app = create_app('prod')
#     with flask_app.app_context():
#         db.create_all()
#     flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))

flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
    flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 50000)))
