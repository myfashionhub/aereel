from models import User


class Users():
    def __init__(self, session):
        self.session = session

    def find_or_create(self, email):
        user = self.session.query(User).filter_by(email=email).first()
        if user:
            return user
        else:
            user = User(email=email)
            self.session.add(user)
            self.session.commit()

        return user
