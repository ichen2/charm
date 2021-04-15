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

from bs4 import BeautifulSoup
import requests

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
    #driver.get("https://vrpreservation.org/wp-admin/post-new.php?calypsoify=1&block-editor=1&frame-nonce=1618551653%3A200109096%3Ad73f51864c9abaa87d151a33d88e1a01&origin=https%3A%2F%2Fwordpress.com&environment-id=production&support_user=&_support_token=")
    driver.find_element_by_class_name("is-primary").click()
    time.sleep(10)

    driver.find_element_by_id("post-title-0").send_keys(title)
    driver.find_element_by_class_name("block-editor-default-block-appender__content").click()
    driver.find_element_by_class_name("block-editor-rich-text__editable").send_keys("/tour\n")
    driver.find_element_by_id("inspector-text-control-1").send_keys(link)
    driver.find_element_by_id("inspector-text-control-2").send_keys(description)
    driver.find_element_by_xpath('//button[contains(text(), "Post")]').click()
    driver.find_element_by_xpath('//button[contains(text(), "Tags")]').click()
    driver.find_element_by_css_selector('input.components-form-token-field__input').send_keys("tag1,tag2,tag3\n")
    driver.find_element_by_xpath('//button[contains(text(), "Featured image")]').click()
    driver.find_element_by_xpath('//button[contains(text(), "Set featured image")]').click()
    
    uploadImage = driver.find_element_by_xpath('//button[contains(text(), "Select Files")]')
    uploadImage.send_keys("/Users/ichen/VRPreservation/post-generator/images/tut.jpg")
    print(uploadImage)

def uploadPost():
    driver.find_element_by_class_name("editor-post-publish-panel__toggle").click()
    driver.find_element_by_class_name("editor-post-publish-button").click()
    time.sleep(3)

login()
createPost('testing', 'testing', 'https://www.google.com')
# soup = BeautifulSoup(open("staging.html"), "html.parser")
# images = []
# for img in soup.findAll('img'):
#     images.append(img.get('src'))

# print(images)

# for i in range(0, len(images)):
#     img_data = requests.get(images[i]).content
#     with open('images/image' + str(i) + '.jpg', 'wb') as handler:
#         handler.write(img_data)
# login()
# with open(CSV_PATH, 'r') as read_obj:
#     csv_reader = DictReader(read_obj)
#     for row in csv_reader:
#         print('creating post...')
#         createPost(row['Title'], row['Site Description'], row['Link'])
