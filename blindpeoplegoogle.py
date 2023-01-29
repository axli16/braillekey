from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.chrome.service import Service
import requests
import pandas as pd 
from bs4 import BeautifulSoup

links = []
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# PATH = r"C:\Users\raymo\Documents\Coding-Programs\chromedriver.exe"
# s=Service(PATH)
# driver = webdriver.Chrome(service=s)
driver.get('https://www.google.com/')

def getdata(url):
    r = requests.get(url)
    return r.text

dictionary = {}
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )
finally:
    search = driver.find_element(By.CLASS_NAME, "gLFyf")
    search.send_keys("Hello there")
    search.send_keys(Keys.RETURN)
    # print(dictionary)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//a[@href]'))
        )
    finally:
        url = driver.current_url
        
        def getdata(url):
            r = requests.get(url)
            return r.text

        htmldata = getdata(url)
        soup = BeautifulSoup(htmldata, 'html.parser')
        data = ''

        x = []
        for data in soup.find_all("a"): #scrapes all the buttons 
            buttons = data.get_text()
            x.append(buttons)

        links = []
        for link in soup.findAll('a'):
            links.append(link.get('href'))

        for i in range(len(x)):
            dictionary[x[i]] = links[i]

print(dictionary)
time.sleep(5)
driver.quit()