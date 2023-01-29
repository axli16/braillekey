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
import speech_recognition as sr
import time
import braille

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
input("Press any button to start...")

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        u_in = r.recognize_google(audio_text)
        print("Text: "+u_in)
    except:
         print("Sorry, I did not get that")
    
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
    search.send_keys(u_in)
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
        
        del x[0:24]

        links = []
        for link in soup.findAll('a'):
            links.append(link.get('href'))
        
        del links[0:24]

        for i in range(len(x)):
            dictionary[x[i]] = links[i]
    for i in range(len(x)):
        print(braille.textToBraille(x[i]))

on_scr = []
for i in range(0,3):
    on_scr.append(x[i])

print(on_scr)

j = 0

while True:
    user_input = input("Input: ")
    if user_input == '1':
        url = dictionary[on_scr[0]]
        break
    elif user_input == '2':
        url = dictionary[on_scr[1]]
        break
    elif user_input == '3':
        url = dictionary[on_scr[2]]
        break
    elif user_input == 'w' and j>0:
        j -= 1
        on_scr[2] = on_scr[1]
        on_scr[1] = on_scr[0]
        on_scr[0] = x[j]
    elif user_input == 's' and j< len(x)-3:
        j += 1
        on_scr[0] = on_scr[1]
        on_scr[1] = on_scr[2]
        on_scr[2] = x[j]
    print('On screen: ', on_scr)
    print(x[j])
        
# print(url)
htmldata = getdata(url.strip('/url?q='))
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''

#Scrapes the title
title = soup.find("h1").get_text()

print(braille.textToBraille(title))

for data in soup.find_all("p"): #scrapes the paragraph texts
    para = data.get_text()
    print(braille.textToBraille(para))
    # print(para)

driver.quit()

