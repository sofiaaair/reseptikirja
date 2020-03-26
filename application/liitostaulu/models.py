from application import db

class KayttajaResepti(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), nullable=False)
    resepti_id = db.Column(db.Integer, db.ForeignKey('resepti.id'), nullable=False)

    def __init__(self, kayttaja_id, resepti_id):
        self.kayttaja_id = kayttaja_id
        self.resepti_id = resepti_id
