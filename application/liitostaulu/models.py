from application import db


from sqlalchemy.sql import text

liitostaulu = db.Table('liitostaulu',
     db.Column('kayttaja_id', db.Integer, db.ForeignKey('kayttaja.id'), primary_key=True),
     db.Column('resepti_id', db.Integer, db.ForeignKey('resepti.id'), primary_key=True)
)



