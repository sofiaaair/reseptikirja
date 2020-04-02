from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.raakaaine.models import RaakaAine
from application.raakaaine.forms import RaakaaineForm

@app.route("/raakaaine", methods=["GET"])
def raakaaine_index():
    return render_template("raakaaine/list.html", raakaaine = RaakaAine.query.all())


@app.route("/raakaaine/new/")
@login_required
def raakaaine_form():
    return render_template("raakaaine/new.html", form = RaakaaineForm())

@app.route("/raakaaine/", methods=["POST"])
@login_required
def raakaaine_create():
    form = RaakaaineForm()

    r = RaakaAine(form.name.data)

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("raakaaine_index"))
