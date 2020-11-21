from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# create instance of Flask app
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars"
mongo = PyMongo(app)


# create route that renders index.html template
@app.route("/", methods=['GET'])
def index():
    mars_mongo_db = mongo.db.mars_mongo_db.find_one()
    return render_template("indext.html", mars = mars_mongo_db)
    
@app.route("/scrape", methods=['GET'])
def scrape():
    mars_mongo_db = mongo.db.mars_mongo_db
    mars_data = scrape_mars.scrape()
    mongo.db.mars_mongo_db.update({}, mars_data, upsert=True)
    return redirect ("/", code=302)
        
if __name__ == "__main__":
    app.run(debug=True)