from application import db

from application.models import Base, Nimellinen


class RaakaAine(Base, Nimellinen):

    kayttajaraakaaine = db.relationship('Resepti', secondary='liitostaulu', lazy='subquery', backref=db.backref('raakaaine', lazy=True))


    def __init__(self, name):
        self.name = name

