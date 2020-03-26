from application import db

class Resepti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    kayttajaresepti = db.relationship("KayttajaResepti", backref='resepti', lazy=True)

    def __init__(self, name):
        self.name = name

