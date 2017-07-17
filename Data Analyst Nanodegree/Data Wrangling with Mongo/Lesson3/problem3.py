#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the
"areaLand" field, you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""

import codecs
import csv
import json
import pprint
import re

CITIES = 'cities.csv'

def is_int(string):
    """Returns True if if the value can be cast to int"""
    try:
        int(string)
        return True
    except ValueError:
        return False

def is_float(string):
    """Returns True if if the value can be cast to float"""
    try:
        float(string)
        return True
    except ValueError:
        return False

def value_type(string):
    if string.startswith('{'):
        return type([])
    elif (string == 'NULL' or string == ''):
        return type(None)
    elif is_int(string):
        return type(1)
    elif is_float(string):
        return type(1.1)
    else:
        return type('s')

def fix_area(area):
    # YOUR CODE HERE
    if value_type(area) == type([None]):
        area = None

    elif value_type(area) == type([]):
        entries = re.split('[{|}]', area)[1:3]

        first, second = entries[0], entries[1]

        try:
            if len(first.split('.')[1]) >= len(second.split('.')[1]):
                area = first
            else:
                area = second
        except:
            if len(first) >= len(second):
                area = first
            else:
                area = second

    return area



def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            # if "areaLand" in line:
            #     line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(3, 20):
        print pprint.pprint(data[n]['name'])

    # assert data[3]["areaLand"] == None
    # assert data[8]["areaLand"] == 55166700.0
    # assert data[20]["areaLand"] == 14581600.0
    # assert data[33]["areaLand"] == 20564500.0


if __name__ == "__main__":
    test()
