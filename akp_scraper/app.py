import requests, datetime, threading, os, urllib.request
from bs4 import BeautifulSoup
from instabot import Bot 

bot = Bot()
# bot.login()
current_headline = ""
current_image = "" 

def scrap_akp():
    response = requests.get("https://www.allkpop.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    global current_headline, current_image
    headlines = soup.select(".title")
    images = soup.select(".image")
    categories = soup.select(".category")
    newest_headline = headlines[1].select(".h_a_i")[0].getText()
    imageurl = images[1].select(".b-lazy")[0].get("data-src")
    category = categories[1].getText()
    if (imageurl[-4:] == "jpeg"):
        imagename = "image." + imageurl[-4:]
    else:
        imagename = "image." + imageurl[-3:]
    
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    if newest_headline == current_headline:
        if current_image:
            try:
                os.remove(current_image +".REMOVE_ME")
            except:
                os.remove(current_image)
            current_image = ""
        print(f"still same news: {current_headline}, category: {category}")

    else:
        if category == "News":
            current_headline = newest_headline
            current_image = imagename
            print(f"updated headline: {current_headline}, category: {category}")
            urllib.request.urlretrieve(imageurl, imagename)
            bot.upload_photo(imagename, 
                    caption = f"{current_headline}. Source: allkpop")
        else:
             current_headline = newest_headline
             print(f"No update: {newest_headline}, category: {category}")

        
        # download pics, update instagram pics, delete pics
        # redo this operation after 5 mins

    threading.Timer(60 ,scrap_akp).start()
