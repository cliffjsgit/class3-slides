#!/usr/bin/python3
#
# Example of a starting project for scraping and saving images from a Web site
#

from bs4 import BeautifulSoup
import os
import requests

URL = "http://www.energyhive.com/"
#URL = "https://www.python.org/"

print("\nHTML Parsing", URL)

page = requests.get(URL).text
soup = BeautifulSoup(page, 'html.parser')

current = os.listdir(path='.')

for item in soup.find_all('img'):
    print("  Image:", item.get('src').split('/')[1])
    if item.get('src').split('/')[1] not in current:
        r = requests.get(URL + item.get('src'), allow_redirects=True)
        open(item.get('src').split('/')[1] , 'wb').write(r.content)
        print('    Downloaded ' + item.get('src').split('/')[1])
    else:
        print('    Already downloaded ' + item.get('src').split('/')[1])
