import selenium
from selenium import webdriver
import time
import io
import requests
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import csv

driver = webdriver.Chrome('chromedriver')

main_url = 'https://wordpress.com/posts/vrpreservation.org/'

driver.get(main_url)
""" for url in page_urls:
driver.get(url)
try:
    iframe = driver.find_element_by_id('mp-iframe')
    tour_url = iframe.get_attribute('src')
    header = driver.find_element_by_class_name('entry-header')
    tour_title = header.text
    if (tour_url != None) and (tour_title != ""):
        tours.append([tour_title, tour_url])
except NoSuchElementException:
    print("mp-iframe not found at " + url)

with open('urls.csv', mode='w', encoding="utf-8") as csv_file:
writer = csv.DictWriter(csv_file, fieldnames=['name', 'url'], lineterminator = '\n')
for tour in tours:
    writer.writerow({'name': tour[0], 'url': tour[1]}) """