from flask_wtf import FlaskForm
from wtforms import StringField, validators, BooleanField

from flask_login import current_user

from application.auth.models import Kayttaja

class ReseptiForm(FlaskForm):
    name = StringField("Reseptin nimi", [validators.Length(min=3)])
    tekija= StringField("Reseptin tekijä, (koko nimi, esim. Ada Lovelace)")

    class Meta:
        csrf = False


class ReseptiEditForm(FlaskForm):
    name = StringField("Muutettavan reseptin nimi", [validators.Length(min=3)])
    newname = StringField("Uusi reseptin nimi", [validators.Length(min=3)])
    class Meta:
        csrf = False
