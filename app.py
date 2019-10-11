from flask import Flask, jsonify
from sqlalchemy.orm import scoped_session, sessionmaker

from db.model import  Studiji, Termin, engine
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db?check_same_thread=False'
app = Flask(__name__)


session = scoped_session(sessionmaker(bind=engine))


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
         "pocetak": termin.startTime,
         "kraj": termin.endTime}
        for termin in termini])

if __name__ == '__main__':
    app.run(host='0.0.0.0')