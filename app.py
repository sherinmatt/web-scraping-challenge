from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#instance of Flask
app = Flask(__name__)

#using Pymongo to establish Mongo connection below
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_application")

#route: template ->index.html
@app.route("/")

def index():
    

