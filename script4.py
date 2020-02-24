# import dependencies
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
import selenium
import io
import pandas as pd
import urllib.request
import urllib.parse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from _datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv


options = webdriver.ChromeOptions()
options.headless=False

driver = webdriver.Chrome("/Users/rishi/Downloads/chromedriver 3")
driver.maximize_window()
prefs = {"profile.default_content_setting_values.notifications" : 2} 
options.add_experimental_option("prefs", prefs)

#open up website
driver.get(
    "https://www.tripadvisor.com/Hotel_Review-g28970-d84078-Reviews-Hyatt_Regency_Washington_on_Capitol_Hill-Washington_DC_District_of_Columbia.html#/media/84078/?albumid=101&type=2&category=101")

# wait until element is found and then store all webelements into list
images = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, '//*[@class="media-viewer-dt-root-GalleryImageWithOverlay__galleryImage--1Drp0"]')))

image_url = []

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
print("Length of page is:", lenOfPage)

driver.execute_script("arguments[0].scrollIntoView();", images[-1])

#iterate through images and acquire their url based on background image style
for index, image in enumerate(images):
    image_url.append(images[index].value_of_css_property("background-image"))

#clean the list to provide clear links
for i in range(len(image_url)):
    start = image_url[i].find("url(\"") + len("url(\"")
    end = image_url[i].find("\")")
    print(image_url[i][start:end])
    image_url[i] = image_url[i][start:end]

#write to csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for image in image_url:
        writer.writerow([image])

