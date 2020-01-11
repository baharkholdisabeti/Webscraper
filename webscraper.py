# Bahar Kholdi-Sabeti
# Jan. 11, 2020
# Web scraper for illness and treatment data
from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.nhsinform.scot/illnesses-and-conditions/a-to-z#D'
response = requests.get(url, timeout=5)
soup = BeautifulSoup(response.content, "html.parser")
illnessArr = []

# all illnesses have h2 tags and are in class "module__title"
# here we will fetch the illness titles
for illnesses in soup.findAll('a', attrs={"class": "col small-12 medium-6 large-4 module"}):
    illnessObject = {
        "title": illnesses.find('h2', attrs={"class": "module__title"}).text
    }
    #print(illnessObject)
    illnessArr.append(illnessObject)

with open('scraperData.json', 'w') as outfile:
    json.dump(illnessArr, outfile)
