from bs4 import BeautifulSoup as Bs

import requests


def west_l():
    url = "https://www.westlotto.de/lotto-6aus49/gewinnzahlen/gewinnzahlen.html"

    respons = requests.get(url)
    html = respons.text

    soup = Bs(respons.content, "html.parser")

    #english_words = soup.find("div", id="random_word").text.strip()
    text = soup.find("ul", class_="mod-simple-list__plain")
    #for a in text:
    print(text)
