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

driver.get("https://www.tripadvisor.ca/Hotels")

time.sleep(1)

#waits for that amount of time
driver.implicitly_wait(12)
#find the searchbar and then plug in the key
driver.find_element_by_xpath('//*[@class="typeahead_input"]').send_keys("Washington D.C.", Keys.ENTER)
#wait
time.sleep(1)
#list all of the hotels in that page
hotels = driver.find_elements_by_xpath('//*[@class="listing_title"]')

print("Total Number of Hotels: ", len(hotels))

#work with the first hotel website first
hotels[0].click()
#get the traver images element
travelerimg = driver.find_elements_by_xpath('//*[@class="hotels-hotel-review-atf-photos-media-window-Albums-Overlay__imageOverlay--1dPs0 hotels-hotel-review-atf-photos-media-window-Albums-Overlay__imageOverlayGray--2vR4q"]')
#click on it
print("Length of list:", travelerimg)

#iterate through each hotel
# for hotel in hotels:
#     #click on each hotel
#     hotel.click()
#     #click on the traveler images
#     traveler_imgs = driver.find_elements_by_xpath('//*[@class="hotels-hotel-review-atf-photos-media-window-Albums-Overlay__imageOverlay--1dPs0 hotels-hotel-review-atf-photos-media-window-Albums-Overlay__imageOverlayGray--2vR4q"]')
    
# for link in traveler_imgs:
#     link = link.click()
    #print(hotel)

#automate searching for hotels in specific city
# driver.find_element_by_xpath('/html/body/div[2]/div/div[6]/div[1]/div/div/div/div/span[1]/div/div/div/a').click() #clicks on hotels option
# driver.implicitly_wait(12) #allows xpath to be found
# driver.find_element_by_xpath('//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[12]/div/div/div[1]/div[1]/div/input').send_keys("Washington D.C.", Keys.ENTER) #change string to get certain city
# time.sleep(8)

# #now get current url
# url = driver.current_url

# response = requests.get(url)
# response = response.text
# data = BeautifulSoup(response, 'html.parser')

# #get list of all hotels
# hotels = driver.find_elements_by_class_name("prw_rup prw_meta_hsx_responsive_listing ui_section listItem")

# print("Total Number of Hotels: ", len(hotels))