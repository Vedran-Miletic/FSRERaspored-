from rasporedparser.termin import parsiraj
from db.model import session, Studiji, Termin
from tqdm import tqdm


session.query(Termin).delete()
session.commit()


studiji = session.query(Studiji).all()

for studij in tqdm(studiji):
    parsiraj(studij)
