from distutils.debug import DEBUG
import os

class Config(object):
    SQLALCHEMY_DATABASE_URL= os.getenv('DATABASE_URL')
    DEBUG = os.getenv('DEBUG')