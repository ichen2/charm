import selenium
import os
from selenium import webdriver
import time
import io
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import csv
from csv import reader
from csv import DictReader

MAIN_URL = 'https://wordpress.com/posts/vrpreservation.org/'
MY_USERNAME = os.environ['WORDPRESS_USERNAME']
MY_PASSWORD = os.environ['WORDPRESS_PASSWORD']
CSV_PATH = './test.csv'

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(10)

# login
driver.get(MAIN_URL)
driver.find_element_by_id("usernameOrEmail").send_keys(MY_USERNAME)
driver.find_element_by_class_name("is-primary").click()
driver.find_element_by_id("password").send_keys(MY_PASSWORD)
driver.find_element_by_class_name("is-primary").click()

time.sleep(3)

# go to posts page
driver.find_element_by_class_name("is-primary").click()

time.sleep(10)

# create post
driver.find_element_by_id("post-title-0").send_keys("Automated Post")
driver.find_element_by_class_name("block-editor-default-block-appender__content").click()
driver.find_element_by_class_name("block-editor-rich-text__editable").send_keys("This post was create using an automated post creation tool!")
driver.find_element_by_class_name("editor-post-publish-panel__toggle").click()
driver.find_element_by_class_name("editor-post-publish-button").click()

""" with open(CSV_PATH, 'r') as read_obj:
    csv_reader = DictReader(read_obj)
    for row in csv_reader:
        print(row['title']) """
