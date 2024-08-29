import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")

quotes_list = []

for i in range(0, len(quotes)):
    tagsforquote = tags[i].find_all("a", class_="tag")
    tags_list = []
    for tagforquote in tagsforquote:
        tags_list.append(tagforquote.text)

    quotes_list.append(
        {"tags": tags_list, "author": authors[i].text, "quote": quotes[i].text}
    )



if __name__ == "__main__":
    with open("qoutes.json", "w", encoding="utf-8") as file:
        json.dump(quotes_list, file)

#     with open("Task_2\qoutes.json", "r", encoding="utf-8") as f:
#         data_from_file = json.load(f)
#         print(data_from_file)
