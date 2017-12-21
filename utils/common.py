from enum import Enum
import simplejson as json
import os


class TwitterUserState(Enum):
    FOUND = 1
    NOT_FOUND = 2 # deleted (or never existed)
    SUSPENDED = 3
    PROTECTED = 4

class DbEngine:
    def __init__(self, config_path):
        self.config_path = config_path

    def new_session(self):
        with open(self.config_path, "r") as config:
            DBCONFIG = json.loads(config.read())

        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        from app.models import Base

        ENV = os.environ['CS_ENV']
        connect_args = {
            'ssl': { 'verify_ssl_cert': True, 'ssl_cipher': 'DHE-RSA-AES256-SHA' }
        } if ENV == 'production' else None

        db_engine = create_engine("mysql://{user}:{password}@{host}/{database}".format(
            host = DBCONFIG['host'],
            user = DBCONFIG['user'],
            password = DBCONFIG['password'],
            database = DBCONFIG['database']), pool_recycle=3600, connect_args=connect_args)

        Base.metadata.bind = db_engine
        DBSession = sessionmaker(bind=db_engine)
        db_session = DBSession()
        return db_session
