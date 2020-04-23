from application import db


from sqlalchemy.sql import text

liitostaulu = db.Table('liitostaulu',
     db.Column('raakaaine_id', db.Integer, db.ForeignKey('raakaaine.id'), primary_key=True),
     db.Column('resepti_id', db.Integer, db.ForeignKey('resepti.id'), primary_key=True)
)



