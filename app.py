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
app.config["SQLALCHEMY_DATABASE_URI"] ="postgres://ccgivigwjxbere:1bfedd860f5c35f65c9a0d4b83338fa773435bab7e6abd239995eb665d7525ee@ec2-34-192-58-41.compute-1.amazonaws.com:5432/dckeb4ijeh54v1"

    ###"postgresql+psycopg2://rjpiahymehlivg:f7a5782c5902a22cc06937aa671847309ddc93152dc6c717980340d15d77ca90@ec2-54-144-251-233.compute-1.amazonaws.com:5432/ddq3qrme7kt4uj"


##    "postgres://pwmrbjlscczizl:b2f0f0dc26e300ec4bee114242916bd8b9d35a6fdbad6a61de016afff6e1a25c@ec2-3-214-3-162.compute-1.amazonaws.com:5432/d2o9bn1u3iguun"

####"postgres://rjpiahymehlivg:f7a5782c5902a22cc06937aa671847309ddc93152dc6c717980340d15d77ca90@ec2-54-144-251-233.compute-1.amazonaws.com:5432/ddq3qrme7kt4uj"

    ##"postgresql+psycopg2://postgres:Vovik20121985@localhost/for_second_stepic"
##"postgresql+psycopg2://postgres:Vovik20121985@localhost/for_second_stepic"
####<Диалект БД>+<Драйвер>://<Имя пользователя>:<Пароль>@<Хост БД>:<Порт>/<Имя БД>



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