from flask import Flask, render_template
from func import *
app = Flask(__name__)

@app.route('/')
def home():
    current_weather_info = weather("tbody", "table table--left table--inner-borders-rows", "https://www.timeanddate.com/sun/india/mathura")
    daily_quote = daily()
    date_today = date_()
    return render_template('index.html', current_weather_info = current_weather_info,len_weather = len(current_weather_info), quote = daily_quote, date = date_today)

@app.route("/news")
def news_():
    date_today = date_()
    world_news = news("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen")
    country_news = news("https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen")
    local_news = news("https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNREZ3Y25nMWVnc0tDUzl0THpBeGNISjROU2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNREZ3Y25nMUtBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen")
    return render_template('news.html', world_news = world_news, len_world = len(world_news), country_news = country_news, len_country = len(country_news), local_news = local_news, len_local = len(local_news), date = date_today)


if __name__ == '__main__':
   app.run()
   