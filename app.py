from flask import Flask, render_template
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from data import teachers_info
import json
import os




app = Flask(__name__)
app.secret_key = "randomstring"

#try:
#    conn = psycopg2.connect("dbname='for_second_stepic' user='postgres' host='localhost' password='Vovik20121985'")
#    print("Very good!!!")
#except:
#    print("I am unable to connect to the database")



#app.config['SQLALCHEMY_DATABASE_URI'] = conn
####app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#print(os.environ.get("DATABASE_URL"))
#app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] ="postgres://qizllymyyraymu:a7d672dfe0d3a5b3cfd838e60bb08779900fe7e1f322861740efa821b02e513f@ec2-34-194-215-27.compute-1.amazonaws.com:5432/d53vfa2588029"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    about = db.Column(db.String, unique=True)
    rating = db.Column(db.String)
    picture = db.Column(db.String, unique=True)
    price = db.Column(db.Integer)
    goals = db.Column(db.String)
    free =  db.Column(db.String)
    bookings = db.relationship("Booking", back_populates='teacher')




class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    name_client = db.Column(db.String)
    phone = db.Column(db.String)
    day_in_week= db.Column(db.String)
    time_to_study = db.Column(db.String)
    teacher = db.relationship("Teacher")
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))



class Proposoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_client = db.Column(db.String)
    phone = db.Column(db.String)
    trainer = db.Column(db.String)
    radio_field_week = db.Column(db.String)

class Goals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_in_english = db.Column(db.String)
    name_in_russian = db.Column(db.String)


for i in range(len(teachers_info)):
    teacher = Teacher(name=(teachers_info[i])["name"],
                     about=(teachers_info[i])["about"],
                      rating=(teachers_info[i])["rating"],
                      picture=(teachers_info[i])["picture"],
                      price=(teachers_info[i])["price"],
                      goals=json.dumps((teachers_info[i])["goals"]),
                      free=json.dumps((teachers_info[i])["free"]))
    db.session.add(teacher)
    db.session.commit()