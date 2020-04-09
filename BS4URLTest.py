import requests
from bs4 import BeautifulSoup

URL = "http://dataquestio.github.io/web-scraping-pages/simple.html"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
