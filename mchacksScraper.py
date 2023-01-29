import requests
import pandas as pd 
from bs4 import BeautifulSoup

dictionary = {}

# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text
url = "https://www.cbc.ca/news/world/russia-air-defence-moscow-ukraine-1.6727196"

htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''

#Scrapes the title
title = soup.find("h1").get_text()

for data in soup.find_all("p"): #scrapes the paragraph texts
    para = data.get_text()
    # print(para)

x = []
for data in soup.find_all("a"): #scrapes all the buttons 
    buttons = data.get_text()
    x.append(buttons)
    #print(x)

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

for i in range(len(x)):
    dictionary[x[i]] = links[i]

print(dictionary)
#print(links)