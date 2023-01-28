import requests
import pandas as pd
from bs4 import BeautifulSoup
  
# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text
url = "https://www.cbc.ca/news/world/russia-air-defence-moscow-ukraine-1.6727196"

htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''

title = soup.find("h1").get_text()
print(title)

for data in soup.find_all("p"):
    para = data.get_text()
    print(para)