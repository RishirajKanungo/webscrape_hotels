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

def parse_style_attribute(style_string):
    if 'background-image' in style_string:
        style_string = style_string.split(' url("')[1].replace('");', '')
        return style_string
    return None


#setup opening url window of website to be scraped
options = webdriver.ChromeOptions()
options.headless=False
prefs = {"profile.default_content_setting_values.notifications" : 2} 
options.add_experimental_option("prefs", prefs)
#driver = webdriver.Chrome("/Users/rishi/Downloads/chromedriver 3") #possible issue by not including the file extension
# driver.maximize_window()
# time.sleep(5)
# driver.get("""https://www.tripadvisor.com/""") #get the information from the page

driver = webdriver.Chrome("/Users/rishi/Downloads/chromedriver 3")
driver.maximize_window()

driver.get("https://www.tripadvisor.com/Hotel_Review-g28970-d84078-Reviews-Hyatt_Regency_Washington_on_Capitol_Hill-Washington_DC_District_of_Columbia.html#/media/84078/?albumid=101&type=2&category=101")

time.sleep(1)

#waits for that amount of time
driver.implicitly_wait(12)
#find the searchbar and then plug in the key
#driver.find_element_by_xpath('//*[@class="typeahead_input"]').send_keys("Washington D.C.", Keys.ENTER)
#wait
time.sleep(1)
#list all of the hotels in that page
images = driver.find_elements_by_xpath('//*[@class="media-viewer-tile-gallery-v2-TileGallery__entryInner--JaADY "]')

image_url = []

for i in range(len(images)):
    image_url.append(images[i].value_of_css_property("background-image"))

print("Total Number of images: ", len(images))
# print(images)

firstimage = images[0].get_attribute("innerHTML")
print(firstimage)

for i in range(len(image_url)):
    print(image_url[i])
