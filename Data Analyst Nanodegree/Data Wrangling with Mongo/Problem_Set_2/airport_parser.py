import requests
from bs4 import BeautifulSoup as bs

import os
os.chdir('/Users/admin/Desktop/Udacity_Github/Data Analyst Nanodegree/Data Wrangling with Mongo/Problem_Set_2')
airportList = []

with open('VX_and_BOS.html', 'r') as html:
    sp = bs(html, 'lxml')
    airportLayer = sp.find(id='AirportList')
    for airport in airportLayer.find_all('option'):
        if 'All' in airport['value']:
            continue
        airportList.append(airport['value'])

print airportList
