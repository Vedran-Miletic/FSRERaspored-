
from sqlalchemy import create_engine, ForeignKey,Column, Integer
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db


Model = declarative_base()

# create an engine
engine = create_engine('sqlite:///baza.db')

Model.metadata.bind = engine
# create a configured "Session" class
Session =scoped_session(sessionmaker(bind=engine))

# create a Session
session = Session()

class Studiji(Model):
    __tablename__='studiji'
    id=Column(Integer, primary_key=True)
    naziv= Column(String(250),nullable=False)
    godina= Column(Integer,nullable=False)
    url = Column(String(250), nullable=False)

class Termin(Model):
    __tablename__ = 'termini'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.String(32))
    date = db.Column('date', db.String)
    startTime= db.Column('startTime', db.String)
    endTime= db.Column('endTime', db.String)
    duration = db.Column('duration', db.Float)
    studiji_id=  Column(Integer, ForeignKey('studiji.id'))
    person = relationship(Studiji)


Model.metadata.create_all(engine)

