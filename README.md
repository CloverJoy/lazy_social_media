# lazy_social_media
Just learned python last week, and this is my very first pyhon app. Overall, Python is fun!! I made Webscraper and Instagram post automation with python powered by beautifulsoup4 and instabot. In this repo, I scrape allkpop.com's newest news every 1 minute. 
If there is a new news, it automatically posts that news (sometimes the pics dimension is not compatible, if that happens, skip to the other news). Credit to https://www.allkpop.com/ to provide all the news!
## prerequisite
Python 3 and pipenv 
```pip install pipenv```

## How to start
1. After forking this repo ```cd lazy_social_media```
2. Install all the depedencies ```pipenv install``` after that run the pipenv shell ```pipenv shell```
3. Then run the program by ```python app.py```
4. for the first timer, uncomment the bot.login line inside akp_scraper/app.py then Follow the prompt from Instabot, happy posting!
5. If not, comment that line, Happy posting!
