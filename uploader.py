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
driver.implicitly_wait(20)

def login():
    driver.get(MAIN_URL)
    driver.find_element_by_id("usernameOrEmail").send_keys(MY_USERNAME)
    driver.find_element_by_class_name("is-primary").click()
    driver.find_element_by_id("password").send_keys(MY_PASSWORD)
    driver.find_element_by_class_name("is-primary").click()

def createPost(title, description, link):
    time.sleep(3)
    driver.get("https://vrpreservation.org/wp-admin/post-new.php?calypsoify=1&block-editor=1&frame-nonce=1617422855%3A200109096%3Ac983ca2a0681a067948225ecaffe0d1e&origin=https%3A%2F%2Fwordpress.com&environment-id=production&support_user=&_support_token=")
    #driver.find_element_by_class_name("is-primary").click()
    time.sleep(10)
    #driver.find_element_by_class_name("is-loaded")
    driver.find_element_by_id("post-title-0").send_keys(title)
    driver.find_element_by_class_name("block-editor-default-block-appender__content").click()
    driver.find_element_by_class_name("block-editor-rich-text__editable").send_keys("/tour\n")
    driver.find_element_by_id("inspector-text-control-1").send_keys(link)
    driver.find_element_by_id("inspector-text-control-2").send_keys(description)

    # publish post
    driver.find_element_by_class_name("editor-post-publish-panel__toggle").click()
    driver.find_element_by_class_name("editor-post-publish-button").click()
    time.sleep(3)

#login()
#createPost("Automated Post", "This is an automated post", "https://www.google.com")

login()
with open(CSV_PATH, 'r') as read_obj:
    csv_reader = DictReader(read_obj)
    for row in csv_reader:
        print('creating post...')
        createPost(row['Title'], row['Site Description'], row['Link'])
