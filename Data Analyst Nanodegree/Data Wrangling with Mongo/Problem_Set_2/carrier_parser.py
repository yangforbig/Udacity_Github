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

print carrierList
