from flask_wtf import FlaskForm
from wtforms import StringField, validators, BooleanField, TextAreaField, SelectField

from flask_login import current_user

from application.auth.models import Kayttaja

from application.reseptit.models import Resepti

class ReseptiForm(FlaskForm):
    name = StringField("Reseptin nimi", [validators.Length(min=3, max=30)])
    tekija= StringField("Reseptin tekijä, (koko nimi, esim. Ada Lovelace)")
    kuvaus = TextAreaField("Reseptin ohje", [validators.Length( max=400, message="Ohjekentän tulee sisältää vähintään %(min)d merkkiä ja enintään %(max)d merkkiä")])

    class Meta:
        csrf = False


class ReseptiEditForm(FlaskForm):
    name = StringField("Muutettavan reseptin nimi", [validators.Length(min=3)])
    newname = StringField("Uusi reseptin nimi", [validators.Length(min=3, max=30)])
#    newkuvaus = TextAreaField("Uusi ohje reseptille", [validators.Length(min=3, max=400, message="Ohjekentän tulee sisältää vähintään %(min)d ja enintään %(max)d merkkiä")])

    class Meta:
        csrf = False


#class ReseptiAddForm(FlaskForm):
#    name = SelectField(u'Reseptin nimi', choices=[Resepti.guery.all()])
