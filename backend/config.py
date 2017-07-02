WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://admin:1330871Pp@178.62.38.12/swipestay'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
