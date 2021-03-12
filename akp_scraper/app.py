import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.allkpop.com/")
soup = BeautifulSoup(response.text, "html.parser")

current_headline = ""

headlines = soup.select(".title")
newest_headline = headlines[0].select(".h_a_i")[0].getText()

if newest_headline != current_headline:
    current_headline = newest_headline
    print(f"updated headline: {current_headline}")
    # download pics, update instagram pics, delete pics
    # redo this operation after 5 mins
else:
    print(f"still same news: {current_headline}")
    # redo this operation after 5 mins
