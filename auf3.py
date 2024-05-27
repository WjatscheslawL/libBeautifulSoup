from bs4 import BeautifulSoup as Bs
from googletrans import Translator
import requests


def get_english_words():
    url = "https://randomword.com"
    try:
        respons = requests.get(url)
        soup = Bs(respons.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_def = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_def": word_def
        }

    except ValueError:
        print("Произошла ошибка")


def word_game_rus():
    print("Привет давай поиграем в Угадай Слово")
    while True:
        trans = Translator()
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        # print(f"Word: {word}")
        rus_word = trans.translate(word, dest="ru")
        # print(f"Rus Word: {rus_word.text}")
        word_def = word_dict.get("word_def")
        print(word_def)
        rus_def = trans.translate(word_def, dest="ru")
        print(f"Какое слово означает:  {rus_def.text}")
        # print(f"word - {rus_def}")
        user = input(" Какое слово означает:  ")
        if user == rus_word:
            print("Правильно")
        else:
            print(f"Не правильно, это:  {rus_word.text}")
            print(word)

        play_againe = input("Хочеш попробовать еще раз? y/n ")
        if play_againe == "n":
            print("Нет, ну тогда пока!")
            break


def word_game_eng():
    print("Hallo")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_def = word_dict.get("word_def")
        print(f"word - {word_def}")
        user = input(" was ist das für wort: ")
        if user == word:
            print("richtig")
        else:
            print(f"richtig: {word}")
            print("falsch")

        play_againe = input("Noch mal? y/n")
        if play_againe == "n":
            print("bei!")
            break
