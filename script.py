# importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# target URL to scrap
url = """https://www.tripadvisor.com/Hotel_Review-g30242-d83951-Reviews-Hyatt_Regency_Crystal_City_at_Reagan_National_Airport-Arlington_Virginia.html#/media/83951/?albumid=106&type=2&category=106"""

#request for the website
website = requests.get(url)

#parse the website data and store into 'data'
data = BeautifulSoup(website.content, 'html.parser')

#find all divs with the specified class name
image_data = data.find_all('div', attrs={"class": "media-viewer-gallery-MediaGallery__item--2qFvR"})

#print all of the images in the list
print('Total number of images: ', len(image_data))

#print out all of the images
for image in image_data:
    print(image)

