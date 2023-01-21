import * as requests from 'requests';
import { BeautifulSoup } from 'bs4';
import { Personal } from 'credentials';
import * as json from 'json';

function weather(elem, Class, url) {
  var city, element, headers, htmlContent, location, lst, r, res, result, soup, str, sunrise, sunset, temp, weather;
  r = requests.get(url);
  htmlContent = r.content;
  soup = new BeautifulSoup(htmlContent, "html.parser");
  element = soup.find_all("table", {
    "class_": Class
  });
  str = soup.find(elem).get_text();
  str.strip;
  lst = str.split(" ");
  sunrise = `${lst.slice(-7)[0]}`;
  sunset = `${lst.slice(-3)[0]}`;
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
  };
  city = "Mathuraweather";
  city = city.replace(" ", "+");
  res = requests.get(`https://www.google.com/search?q=${city}&oq=${city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8`, {
    "headers": headers
  });
  soup = new BeautifulSoup(res.text, "html.parser");
  location = soup.select("#wob_loc")[0].getText().strip();
  weather = soup.select("#wob_dc")[0].getText().strip();
  temp = soup.select("#wob_tm")[0].getText().strip();
  temp = `${temp} °C`;
  result = {
    "Location": location,
    "Temprature": temp,
    "Weather": weather,
    "Sunset": sunset,
    "Sunrise": sunrise
  };
  return result;
}

function daily() {
  var author, data, dict, json_data, quote, quote_url, r, sentence;
  quote_url = "https://favqs.com/api/qotd";
  r = requests.get(quote_url);
  data = r.text;
  json_data = json.loads(data);
  quote = json_data["quote"];
  sentence = quote["body"];
  author = quote["author"];
  dict = {
    "\u2764\ufe0f": sentence,
    "Author": author
  };
  return dict;
}

function news(url) {
  var htmlContent, i, length_lst, length_news, lst, news_list, r, soup, text;
  r = requests.get(url);
  htmlContent = r.content;
  soup = new BeautifulSoup(htmlContent, "html.parser");
  news_list = soup.findAll("h4", {
    "class_": "gPFEn"
  });
  length_news = news_list.length;
  lst = [];

  for (var i = 0, _pj_a = length_news; i < _pj_a; i += 1) {
    text = news_list[i];
    lst.append(text.getText());
    i = i + 1;
  }

  length_lst = lst.length;

  for (var i = 0, _pj_a = length_lst; i < _pj_a; i += 1) {
    text = lst[i];
    console.log(text);
    i = i + 1;
  }
}
