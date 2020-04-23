from application import db

from application.models import Base, Nimellinen

from sqlalchemy.sql import text

class Kayttaja(Base, Nimellinen):

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    reseptit = db.relationship('Resepti', backref='kayttaja', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_name(self):
        return self.name

    @staticmethod
    def palauta_kaikki_nimet():
        stmt = text("SELECT Kayttaja.name FROM Kayttaja"
                    " GROUP BY Kayttaja.id")
        res =db.engine.execute(stmt)

        return res
