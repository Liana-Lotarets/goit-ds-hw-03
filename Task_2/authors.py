import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

href = soup.select("[href^='/author/']")
authors_ref_set = set()
for ref in href:
    authors_ref_set.add(ref.attrs["href"])

urls_authors = []
for ref in authors_ref_set:
    urls_authors.append("https://quotes.toscrape.com" + ref)

soups = []
for url in urls_authors:
    soups.append(BeautifulSoup(requests.get(url).text, "lxml"))

authors_list = []

for i in range(0, len(soups)):
    authors_list.append(
        {
            "fullname": soups[i].find_all("h3", class_="author-title")[0].text,
            "born_date": soups[i].find_all("span", class_="author-born-date")[0].text,
            "born_location": soups[i].find_all("span", class_="author-born-location")[0].text,
            "description": soups[i].find_all("div", class_="author-description")[0].text,
        }
    )


if __name__ == "__main__":

    with open("authors.json", "w", encoding="utf-8") as file:
        json.dump(authors_list, file)

