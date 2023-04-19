from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import config

def create_app():
    app = Flask(__name__)
    # client = MongoClient(config.mongo_creds)
    client = MongoClient()
    app.db = client.e_learning_app

    @app.get("/")
    def home():
        return render_template("home.html")
    
    @app.get("/about")
    def about():
        return render_template("about.html")
    
    @app.get("/subjects")
    def subjects():

        entries_subjects = [
            (
                entry["subject_name"],
                 entry["subject_desc"],
                entry["subject_url"]
            )
            for entry in app.db.subjects.find({})
        ]

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
    
    return app