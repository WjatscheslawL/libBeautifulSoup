from bs4 import BeautifulSoup as Bs

import requests

url = "http://quotes.toscrape.com"

respons = requests.get(url)
html = respons.text

soup = Bs(html, "html.parser")

links = soup.find_all("a")
for link in links:
    print(link)
    # print(link.get('href'))
