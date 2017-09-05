import os

# from sqlalchemy import create_engine
import logging

from aereel import app, models
from aereel.config import config

config = config[os.environ['AEREEL_ENV']]

if __name__ == '__main__':
    if config['DEBUG'] == True:
        logging.basicConfig(level=logging.DEBUG)

    # engine = create_engine(app.config['DATABASE_URL'], echo=False)
    # models.Base.metadata.create_all(engine) # Run migration
    app.run(host='0.0.0.0', debug=config['DEBUG'])
