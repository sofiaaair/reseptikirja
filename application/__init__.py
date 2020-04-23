# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tietokanta
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reseptit.db"
    app.config["SQLALCHEMY_ECHO"] = True
#Edellä pyydettiin SQLAlchemyä tulostamaan kaikki SQL-kyselyt

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Oman sovelluksen toiminnallisuudet
from application import views

from application.reseptit import models
from application.reseptit import views

from application.auth import models
from application.auth import views

from application.liitostaulu import models
from application.liitostaulu import views

from application.raakaaine import models
from application.raakaaine import views

# Kirjautuminen
from application.auth.models import Kayttaja
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return Kayttaja.query.get(user_id)


# Luodaan lopulta tarvittavat tietokantataulut
try: 
    db.create_all()
except:
    pass

