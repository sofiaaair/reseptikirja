from flask import render_template

from application import app

from application.liitostaulu.models import liitostaulu

from sqlalchemy.sql import text

from flask_login import current_user


