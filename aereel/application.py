import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config

config = config[os.environ['AEREEL_ENV']]


def create_session():
    engine  = create_engine(config['DATABASE_URL'])
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session
