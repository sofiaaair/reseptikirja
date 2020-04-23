
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.reseptit.models import Resepti
from application.reseptit.forms import ReseptiForm
from application.reseptit.forms import ReseptiEditForm

from sqlalchemy.sql import text

from application.auth.models import Kayttaja

@app.route("/reseptit", methods=["GET"])
@login_required
def reseptit_index():
    return render_template("reseptit/list.html", reseptilista = Resepti.query.all())

@app.route("/reseptit/new/")
@login_required
def reseptit_form():
    return render_template("reseptit/new.html", form = ReseptiForm())

@app.route("/reseptit/edit/")
@login_required
def reseptit_edit():
    return render_template("reseptit/edit.html", form = ReseptiEditForm(), reseptilistanen = Resepti.query.all())

@app.route("/reseptit/<resepti_id>/", methods=["POST"])
@login_required
def reseptit_delete(resepti_id):

    t = Resepti.query.get(resepti_id)
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("reseptit_index"))


@app.route("/reseptit/edit/", methods=["POST"])
def reseptit_change():
    form = ReseptiEditForm(request.form)
    resepti = Resepti.query.filter_by(name = form.name.data).first()
    reseptinen = Resepti.query.get(resepti.id)
    reseptinen.name = form.newname.data;



    if not form.validate():
        return render_template("reseptit/edit.html", form = form)

    db.session().add(resepti)
    db.session().commit()

    return redirect(url_for("reseptit_index"))




@app.route("/reseptit/", methods=["POST"])
@login_required
def reseptit_create():
    form = ReseptiForm(request.form)

    if not form.validate():
        return render_template("reseptit/new.html", form = form)

    t = Resepti(form.name.data)
    t.kuvaus = form.kuvaus.data
    t.kayttaja_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("reseptit_index"))

