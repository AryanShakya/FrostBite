from datetime import date
import requests
from bs4 import BeautifulSoup
from credentials import Personal
import json

def weather(elem, Class, url):   # gets weather info from a website by bs4
    
    # Step 1: Get the HTML
    r = requests.get(url)
    htmlContent = r.content

    # Step 2: Parse the HTML
    soup = BeautifulSoup(htmlContent, 'html.parser')

    # find all the elements with class lead
    element = soup.find_all("table", class_=Class)

    str = (soup.find(elem).get_text())  #String is what we get
    str.strip # removes whitespaces

    lst = str.split(" ")   # converts in list

    sunrise = f"Sunrise - {lst[-7]} "
    sunset = f"Sunset - {lst[-3]} "  # gets the desired elements by index


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
    city = "Mathuraweather"  # scrapes with google.com

    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip() + " "
    weather = soup.select('#wob_dc')[0].getText().strip()+ " "
    temp = soup.select('#wob_tm')[0].getText().strip()+ " "

    temp = f"{temp} °C "

    result = [location, weather, temp, sunrise, sunset]

    return result
    
def daily():
    
    quote_url = "https://favqs.com/api/qotd"
    # getting response object
    r = requests.get(quote_url)		# r variable has all the HTML code
    
    data = r.text	# r returns response so if we want the code we write r.content

    json_data = json.loads(data)

    quote = json_data["quote"]

    # print(quote)

    sentence = quote["body"]
    author = quote["author"]

    dict = {
        "❤️": sentence,
        "Author": author
    }

    return dict #, author

def news(url): #form google_news
    r = requests.get(url)
    htmlContent = r.content

    # Step 2: Parse the HTML
    soup = BeautifulSoup(htmlContent, 'html.parser')

    news_list = soup.findAll("h4", class_ = "gPFEn")

    length_news = len(news_list) 

    lst = []
    
    for i in range(length_news):
        text = news_list[i]
        lst.append(text.getText())
        i = i+1

    # length_lst = len(lst)

    # for i in range(length_lst):
    #     text = lst[i]
    #     return(text)
    #     i = i+1
        
    return lst

def date_():
    # Returns the current local date
    date_today = date.today()
    return date_today
    # print(date_today)
