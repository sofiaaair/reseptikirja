
from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.reseptit.models import Resepti
from application.reseptit.forms import ReseptiForm

@app.route("/reseptit", methods=["GET"])
def reseptit_index():
    return render_template("reseptit/list.html", reseptilista = Resepti.query.all())

@app.route("/reseptit/new/")
@login_required
def reseptit_form():
    return render_template("reseptit/new.html", form = ReseptiForm())

@app.route("/reseptit/<resepti_id>/", methods=["POST"])
@login_required
def reseptit_delete(resepti_id):

    t = Resepti.query.get(resepti_id)
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("reseptit_index"))

@app.route("/reseptit/", methods=["POST"])
@login_required
def reseptit_create():
    form = ReseptiForm(request.form)

    if not form.validate():
        return render_template("reseptit/new.html", form = form)

    t = Resepti(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("reseptit_index"))
