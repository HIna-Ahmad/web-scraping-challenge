#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import os
from flask import Flask, render_template, redirect


# In[2]:


# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[3]:


# Define database and collection
db = client.mars_db
collection = db.items


# In[19]:


executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path)


# In[5]:


url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# In[6]:


# Retrieve page with the requests module
response = requests.get(url)
html = browser.html
# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')


# In[7]:


title = soup.find_all('div', class_='content_title')[1].text
title


# In[8]:


paragraph = soup.find_all('div', class_='article_teaser_body')[0].text
paragraph


# In[20]:


featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(featured_image_url)


# In[18]:


about_url = 'https://space-facts.com/mars/'
dfs = pd.read_html(about_url)


# In[11]:


table2= dfs[1]
table2


# In[12]:


table2_df = table2
table2_df


# In[13]:


about_html_table = table2_df.to_html()
print(about_html_table)


# In[28]:


hemisphere_images_url = [
    {"title":"Cerberus Hemisphere", "img_url":"https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"},
    {"title":"Schiaparelli Hemisphere", "img_url":"https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"},
    {"title":"Syrtis Major Hemisphere", "img_url":"https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"},
    {"title":"Valles Marineris Hemisphere", "img_url":"https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"},
]

hemisphere_images_url


# In[30]:


mars_breakdown = {
    "title": title,
    "paragraph": paragraph,
    "featured_image_url": featured_image_url,
    "about_url": about_url,
    "hemisphere_images_url": hemisphere_images_url
}
mars_breakdown


# In[ ]:




