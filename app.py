from flask import Flask, render_template, request, redirect, url_for
from models.subject import SubjectModel
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

## uncomment to add entries to db
# db = SQLAlchemy(app)

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/subjects")
def subjects():

    subjects = SubjectModel.query.all()

    entries_subjects = [
        (
            entry.name,
            entry.desc
        )
        for entry in subjects
    ]

    return render_template("subjects.html", entries_subjects=entries_subjects)

@app.get("/subject/<subject_name>")
def subject(subject_name):

    courses = CourseModel.query.filter_by(subject_name=subject_name)

    entries_courses = [
        (
            entry.name,
            entry.desc
        )
        for entry in courses
    ]

    return render_template("subject.html", subject_name=subject_name, entries_courses=entries_courses)

@app.get("/course/<course_name>")
def course(course_name):

    course = CourseModel.query.filter_by(name=course_name).first()

    course_name = course.name
    course_desc = course.desc

    videos = VideoModel.query.filter_by(course_name=course_name)

    entries_videos = [
        (
            entry.name,
            entry.desc,
            entry.course_name,
            entry.video_num
        )
        for entry in videos
    ]

    return render_template("course.html", course_name=course_name, course_desc=course_desc, entries_videos=entries_videos)

@app.route("/video/<course_name>/<video_num>", methods = ['POST', 'GET'])
def video(course_name, video_num):

    if request.method == "POST":

        course_name = course_name
        current_video_num = int(video_num)
        movement = request.form['submit_paginate']

        # naive pagination implementation
        # proper pagination out of scope for this project
        if (current_video_num == 1 and movement == 'previous'):
            video_num = 1
        elif (current_video_num == 1 and movement == 'next'):
            video_num = 2
        elif (current_video_num == 2 and movement == 'previous'):
            video_num = 1
        elif (current_video_num == 2 and movement == 'next'):
            video_num = 2

        return redirect(url_for('video', course_name=course_name, video_num=video_num))

    video = VideoModel.query.filter_by(course_name=course_name, video_num=video_num).first()

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