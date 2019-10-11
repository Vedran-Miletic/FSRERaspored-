from flask import Flask, jsonify
from db.model import  session, Studiji, Termin
app = Flask(__name__)

@app.route("/studiji")
def studiji():
    studiji = session.query(Studiji).all()
    return jsonify([
        {"id": studij.id, "naziv":studij.naziv, "godina":studij.godina, "url": studij.url}
        for studij in studiji])


@app.route("/termini/<int:studij_id>")
def termini(studij_id):
    termini = session.query(Termin).filter_by(studiji_id=studij_id).all()
    return jsonify([
        {"id": termin.id,
         "naslov":termin.title,
         "datum":termin.date,
         "trajanje": termin.duration,
         "pocetak": termin.startTime}
        for termin in termini])