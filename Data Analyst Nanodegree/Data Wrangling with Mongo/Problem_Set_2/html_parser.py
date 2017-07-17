# Parse all the Carrier list and Aiport data from
# https://www.transtats.bts.gov/Data_Elements.aspx?Data=2


import requests
from bs4 import BeautifulSoup as bs

import os
os.chdir('/Users/admin/Desktop/Udacity_Github/Data Analyst Nanodegree/Data Wrangling with Mongo/Problem_Set_2')


carrierList = []

with open('VX_and_BOS.html', 'r') as html:
    sp = bs(html, 'lxml')
    carrierLayer = sp.find(id='CarrierList')
    carriers = carrierLayer.find_all('option')
    for carrier in carriers:
        if 'All' in carrier['value']:
            continue
        carrierList.append(carrier['value'])

# Collect airports except for the 'All
airportList = []

with open('VX_and_BOS.html', 'r') as html:
    sp = bs(html, 'lxml')
    airportLayer = sp.find(id='AirportList')
    for airport in airportLayer.find_all('option'):
        if 'All' in airport['value']:
            continue
        airportList.append(airport['value'])

# Parse the data from example web page

def parse_web(carrier, airport):

    s = requests.Session()
    r = s.get('https://www.transtats.bts.gov/Data_Elements.aspx?Data=2')

    soup = bs(r.text, 'lxml')
    viewstate_element = soup.find(id="__VIEWSTATE")
    viewstate = viewstate_element['value']
    eventvalidation_element = soup.find(id="__EVENTVALIDATION")
    eventvalidation = eventvalidation_element['value']
    viewstategenerator_element = soup.find(id="__VIEWSTATEGENERATOR")
    viewstategenerator = viewstategenerator_element["value"]

    r = s.post('https://www.transtats.bts.gov/Data_Elements.aspx?Data=2',
           data = (
           ("__EVENTTARGET", ""),
           ("__EVENTARGUMENT", ""),
           ("__VIEWSTATE", viewstate),
           ("__VIEWSTATEGENERATOR",viewstategenerator),
           ("__EVENTVALIDATION", eventvalidation),
           ("CarrierList", carrier),
           ("AirportList", airport),
           ("Submit", "Submit")
          ))

    with open("{0}_and_{1}.html".format(carrier, airport), "w") as f:
        f.write(r.text)


def main():
    for carrier in carrierList[0:4]:
        for airport in airportList[0:5]:
            parse_web(carrier, airport)


main()
