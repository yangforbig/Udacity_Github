import requests
from bs4 import BeautifulSoup as bs
import os
import re
os.chdir('/Users/admin/Desktop/Udacity_Github/Data Analyst Nanodegree/Data Wrangling with Mongo/Problem_Set_2/datafiles')
# data = [{"courier": "FL",
#          "airport": "ATL",
#          "year": 2012,
#          "month": 12,
#          "flights": {"domestic": 100,
#                      "international": 100}
#         },
#         {"courier": "..."}
# ]


def get_files(datadir):
    files = os.listdir(datadir)
    return files

datafiles = get_files(os.getcwd())
datafiles = datafiles[0:10]
data = []
for datafile in datafiles:

    with open(datafile, 'r') as html:
        page = bs(html, 'lxml')
        rows = page.find_all('tr','dataTDRight')
        for row in rows:
            cells = row.find_all('td')
            values = [cell.text for cell in cells]
            if values[1] == 'TOTAL':
                continue
            entry = {}
            info = re.split("[_.]", datafile)
            entry['courier'], entry['airport'] = info[0], info[2]
            entry['year'] = values[0]
            entry['month'] = values[1]
            entry['flights'] = {'domestic': values[2],
                                'international': values[3]}
            data.append(entry)

print data[0]
