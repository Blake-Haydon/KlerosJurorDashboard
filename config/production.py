from .default import *
import os


if 'RDS_HOSTNAME' in os.environ:
    DATABASE = {
            'ENGINE': 'mysql+pymysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': os.environ['RDS_PORT'],
            'DB': os.environ['DB_NAME']
    }
    SQLALCHEMY_DATABASE_URI = DATABASE['ENGINE']+'://'+DATABASE['USER']+':'+ \
    DATABASE['PASSWORD']+'@'+DATABASE['HOST']+':'+DATABASE['PORT']+'/'+DATABASE['DB']
else:
    raise AttributeError("The RDS Database information was not specified.")


APP_ENV = APP_ENV_PRODUCTION