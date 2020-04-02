from application import db

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)


class Nimellinen(db.Model):

    __abstract__ = True

    name = db.Column(db.String(144), nullable=False)
