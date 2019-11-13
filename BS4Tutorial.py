#!/usr/bin/python3
#
# Example of web page scraping from a web site using BeautifulSoup
# From "Tutorial: Python Web Scraping Using BeautifulSoup"
#   https://www.dataquest.io/blog/web-scraping-tutorial-python/

import requests
from bs4 import BeautifulSoup

# First download the web page's content, using the Python requests library, request.get API
# Python API Tutorial: Getting Started with APIs
#   https://www.dataquest.io/blog/python-api-tutorial/

URL = "http://dataquestio.github.io/web-scraping-pages/simple.html"
print("***************************************************************************")
print("** Web scraping  URL:", URL)
print("** Tutorial: https://www.dataquest.io/blog/web-scraping-tutorial-python/ ")
print("***************************************************************************")

# Get Request the Web Page from the URL
page = requests.get(URL)
# A HTTP get request code 200 is "OK! The request was fulfilled"
print("\n*** HTTP Get request status code:", page.status_code)

print("\n*** Unprocessed Web page HTML content:\n", page.content)

# Use BeautifulSoup to process the HTML page content
soup = BeautifulSoup(page.content, 'html.parser')
print("\n*** Soup prettify:\n", soup.prettify())
print("\n*** process list contents of the page:\n",list(soup.children))

# Select the html tag and its children by taking the third item in the list
html = list(soup.children)[2]
print("\n*** html tag:\n", html)

# Select the body tag and its children by taking the fourth HTML item in the list
body = list(html.children)[3]
print("\n*** body tag:\n", body)

p = list(body.children)[1]
print("\n*** second HTML tag in body (a paragraph):\n", p)
print(p.get_text())


## Finding all instances of a specific tag at once
print("\n\n*** Find all tags that are paragraps:")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p'))

# Note that find_all returns a list, so we’ll have to loop through
# the list, or use list indexing to extract the text:
print("\n**** The first paragraph tag contents, from a find all p tags:")
print(soup.find_all('p')[0].get_text())
# Or find the first instance of a tag, such as a paragraph tag:
print("\n*** The first instance of tag p:\n", soup.find('p'))

