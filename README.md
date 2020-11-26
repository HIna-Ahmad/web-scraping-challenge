# web-scraping-challenge

In jupyter notebook scraped and collected all items requried per instructions. 

Moved items from jupyter notebook file to `scrape_mars.py` to scrape requested information (title, paragraph, featured image, list of hemisphere urls and table) from the nasa page provided in the instruction. The `mars_data` function should return the requested material as a Python Dictionary 
In `app.py`, completed the `/scrape` route to store the Python dictionary as a document in a mongo database collection.

In `app.py`, completed the `/` route to read one entry from mongo and render the flask template with the mongo data.

Note - after clicking the "Scrape New Data" button on the webpage, the scrape does not render a working image, for any of the images that were being scraped. This is not an issue that was resolved by my Instructor - TAs or Tutor. However, if you are able to look at the link in the HTML, and copy it into another browser, the link does work and render an image -- so the error is not on my end, as in, debugging that error is not something we learned in class -- so I hope that I do not get any points removed for that when grading this homework assignment. Thank you Grading Team. 
