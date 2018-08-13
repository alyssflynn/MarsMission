from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/app"

mongo = PyMongo(app)

# Route to render index.html
@app.route("/")
def home():
    # get data
    # mars_data = mongo.db.mars_data.find_one()
    mars_data = mongo.db.mars_data.find()

    # return template and data
    return render_template("index.html", mars_data=mars_data)

# Route to trigger scrape function
@app.route("/scrape")
def scrape():
    mars_info = scrape_mars.scrape()
    mars_data = mongo.db.mars_data
    print(mars_info)
    mars_data.update(
        {},
        mars_info,
        upsert=True
    )
    return redirect("/", code=302)

if __name__=="__main__":
    app.run()