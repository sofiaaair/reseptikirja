from application import db

from sqlalchemy.sql import text

from application.models import Base, Nimellinen

from application.liitostaulu.models import liitostaulu 

class Resepti(Base, Nimellinen):

    kayttajaresepti = db.relationship('Kayttaja', secondary='liitostaulu', lazy='subquery', backref=db.backref('resepti', lazy=True))

    def __init__(self, name):
        self.name = name


    def get_id(self):
        return self.id



