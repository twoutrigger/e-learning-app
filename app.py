from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api
from models.subjects import SubjectsModel
from models.course import CourseModel
from models.video import VideoModel
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

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/subjects")
def subjects():

    subjects = SubjectsModel.query.all()

    print(subjects)

    entries_subjects = [
        (
            entry.name,
            entry.desc,
            entry.url
        )
        for entry in subjects
    ]

    return render_template("subjects.html", entries_subjects=entries_subjects)

@app.get("/course/<course_name>")
def course(course_name):

    # resource for dynamic url
    # https://testdriven.io/tips/619b4748-dc9d-434a-9c11-1f09528a2039/

    course = CourseModel.query.first()

    course_name = course.name
    course_desc = course.desc

    videos = VideoModel.query.all()

    entries_videos = [
        (
            entry.name,
            entry.desc,
            entry.url
        )
        for entry in videos
    ]

    return render_template("course.html", course_name=course_name, course_desc=course_desc, entries_videos=entries_videos)

@app.get("/video/<course_name>/<video_num>")
def video(course_name, video_num):

    #change to .filter().first()
    video = VideoModel.query.first()

    video_name = video.name
    video_desc = video.desc
    video_url = video.url
    return render_template("video.html", video_name=video_name, video_desc=video_desc, video_url=video_url)
    

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    with app.app_context():
        db.create_all()

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)