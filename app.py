from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api
from models.subjects import SubjectsModel
from flask_sqlalchemy import SQLAlchemy
import config
import os

app = Flask(__name__)

app.config['DEBUG'] = True

uri = os.getenv("DATABASE_URL", "sqlite:///data.db")

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = ''
# api = Api(app)

db = SQLAlchemy(app)

class SubjectsModel(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    desc = db.Column(db.String(240))
    url = db.Column(db.String(80))

    def __init__(self, name, desc, url):
        self.name = name
        self.desc = desc
        self.url = url

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Subject {self.name}>'

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/subjects")
def subjects():

    # entries_subjects = [
    #     (
    #         entry["subject_name"],
    #         entry["subject_desc"],
    #         entry["subject_url"]
    #     )
    #     for entry in app.db.subjects.find({})
    # ]

    # print(entries_subjects)

    entries_subjects=[1,2,3]

    return render_template("subjects.html", entries_subjects=entries_subjects)

@app.get("/course/<course_name>")
def course(course_name):

    course_name = 'placeholder'
    course_desc = 'placeholder'

    video_list = [
        (
            entry["video_num"],
            entry["video_name"],
            entry["video_len"],
            entry["video_url"]
        )
        # need to filter for course
        for entry in app.db.videos.find({})
    ]

    return render_template("course.html", course_name=course_name, course_desc=course_desc, video_list=video_list)

@app.get("/video/<course_name>/<video_num>")
def video(course_name, video_num):

    video_name = 'placeholder'
    video_desc = 'placeholder'
    return render_template("video.html", video_name=video_name, video_desc=video_desc)
    
if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)