from application import db

from sqlalchemy.sql import text

from application.models import Base, Nimellinen

from application.liitostaulu.models import liitostaulu 


class Resepti(Base, Nimellinen):

    kuvaus = db.Column(db.String(400))

    kayttaja_id = db.Column(db.Integer, db.ForeignKey('Kayttaja.id'), nullable = False)

    kayttajaraakaaine = db.relationship('RaakaAine', secondary='liitostaulu', lazy='subquery', backref=db.backref('resepti', lazy=True))




    def __init__(self, name):
        self.name = name


    def get_id(self):
        return self.id


    def edit_resepti(request, id):
        resepti = Resepti.query.get(id)
        form = ReseptiEditForm(request.POST, obj=resepti)
        form.group_id.choices = [(r.name) for r in Resepti.query.order_by('name')]



