# config/default.py
from os.path import abspath, dirname
# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'klerosboarddev'
DEBUG = False

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = APP_ENV_PRODUCTION
