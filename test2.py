from bs4 import BeautifulSoup as Bs

import requests


def auf2():
    url = "http://quotes.toscrape.com"

    respons = requests.get(url)
    html = respons.text

    soup = Bs(html, "html.parser")

    text = soup.find_all("span", class_="text")
    print(text)
    author = soup.find_all("small", class_="author")
    print(author)
    for i in range(len(text)):
        # Присвоим номер каждой цитате так, чтобы нумерация шла с 1
        print(f"Цитата номер - {i + 1}")
        # Выводим саму цитату, указывая её id
        print(text[i].text)
        # Выводим автора цитаты
        print(f"Автор цитаты - {author[i].text}\n")
