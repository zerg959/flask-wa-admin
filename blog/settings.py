import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


SECRET_KEY = os.urandom(36) #'my_secret_key'
SQLALCHEMY_DATABASE_URI = os.environ.get(
  'SQLALCHEMY_DATABASE_URI'
  )
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
  'SQLALCHEMY_TRACK_MODIFICATIONS'
  )
