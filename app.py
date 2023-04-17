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
    
    return app