from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
from models import Item, Save, User

def create_session(database_url):
    engine  = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return session

class Database():
    def __init__(self, database_url):
        self.session = create_session(database_url)

    def get_links_with_clicks(self, key):
        links = self.session.query(ShortUrl).filter_by(key=key).all()
        link_ids = [link.id for link in links]

        click_query = self.session.query(Click) \
                      .filter(Click.short_url_id.in_(link_ids)) \
                      .order_by(Click.created_at)

        results = []
        for link in links:
            query = click_query.filter_by(short_url_id=link.id)
            results.append( {
                'link': link,
                'click_total': query.count()
            } )
        return results
