from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ReseptiForm(FlaskForm):
    name = StringField("Reseptin nimi", [validators.Length(min=3)])
 
    class Meta:
        csrf = False
