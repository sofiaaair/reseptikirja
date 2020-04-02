from flask_wtf import FlaskForm
from wtforms import StringField

class LiitostauluForm(FlaskForm):
   tekija_name = StringField("Tekijan nimi")
   resepti_name = StringField("Reseptin nimi")

   class Meta:
       csrf = False
