from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import config

def create_app():
    app = Flask(__name__)
    # client = MongoClient(config.mongo_creds)
    client = MongoClient()
    app.db = client.user_data_appe_learning_app

    @app.get("/")
    def home():
        return render_template("home.html")
    
    @app.get("/about")
    def about():
        return render_template("about.html")
    
    @app.get("/subjects")
    def subjects():
        return render_template("subjects.html")
    
    @app.get("/course/<course_name>")
    def course():
        return render_template("course.html")
    
    @app.get("/video/<course_name>/<video_num>")
    def video():
        return render_template("video.html")
    
    return app