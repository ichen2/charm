ort os
import selenium
from selenium import webdriver
import time
import io
import requests
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome('chromedriver.exe')

main_url = 'http://historyview.org/'
main_page = requests.get(main_url)

main_soup = BeautifulSoup(main_page.content, 'html.parser')

a_tags = main_soup.find_all(class_='image-wrap')
page_urls = list(map(lambda url: url['href'], a_tags))

tours = []

for url in page_urls:
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
for tour in tours:
    print(tour[0] + ", " + tour[1])
    
with open('urls.csv', mode='w', encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['name', 'url'], lineterminator = '\n')
    for tour in tours:
        writer.writerow({'name': tour[0], 'url': tour[1]})