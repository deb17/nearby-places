import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or \
        b'6\xaa\x8bp\xc0y\xb4%\x8eY\x1d\xea\xda\xa4\x122'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'features.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
