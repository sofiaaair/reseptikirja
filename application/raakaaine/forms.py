from flask_wtf import FlaskForm
from wtforms import StringField

class RaakaaineForm(FlaskForm):
    name = StringField("Raaka-aineen nimi")

    class Meta:
       csrf = False
