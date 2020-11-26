from flask import Flask, render_template, redirect
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from selenium import webdriver

# create an instanace of our Flask app.
app = Flask(__name__)

# create connection variable
conn = "mongodb://localhost:27017"

# pass connection to the pymongo instance
client = pymongo.MongoClient(conn)

# connect to a database - it will create one if not already available
db = client.mars

db.mars.drop()

# create collection of mars hemisphere urls
image_url = db.image_url

# select COLLECTION in the db and INSERT DOCUMENTS

image_url.insert_many(
    [
        {
            "title": "Cerberus Hemisphere",
            "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",
        },
        {
            "title": "Schiaparelli Hemisphere",
            "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
        },
        {
            "title": "Syrtis Major Hemisphere",
            "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced",
        },
        {
            "title": "Valles Marineris Hemisphere",
            "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced",
        },
    ]
)


def init_browser():

    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {
        "executable_path": "/Users/hinaahmad/Desktop/drivers/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
    #driver = webdriver.Chrome()


def scrape_info():

    browser = init_browser()
    url = "https: // mars.nasa.gov/news /?page = 0 & per_page = 40 & order = publish_date+desc % 2Ccreated_at+desc & search = &category = 19 % 2C165 % 2C184 % 2C204 & blank_scope = Latest"
    # driver.get("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest")
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    # get the title
    title = soup.find_all("div", class_="content_title")[1].text

    # get the paragraph
    paragraph = soup.find_all("div", class_="article_teaser_body")[0].text

    # get the featured image url
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # Find the element and attribute for the background image
    relative_featimage_path = soup.find_all("img")[1]["src"]

    url_featimage_path = featured_image_url + relative_featimage_path

    # store data in a dictionary

    mars_data = {
        "title": title,
        "paragraph": paragraph,
        "url_geatimage_path": url_featimage_path,
    }

    # close the browser after scraping
    browser.quit()

    return mars_data
