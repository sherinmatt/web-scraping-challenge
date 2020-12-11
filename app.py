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
    mars_record = mongo.db.record_collection.find_one()
    return render_template("index.html", scrape_data = mars_record)
#  flask issues affecting mongo connection

#route scrape() f

@app.route("/scrape")

def scrape():
#issue with running scrape because of flask
    #scrape_data = scrape_mars.scrape()
#need to update the mongodb
    #mongo.db.record_collection.update({}, scrape_data , upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

