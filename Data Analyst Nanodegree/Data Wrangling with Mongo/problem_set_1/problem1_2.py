# -*- coding: utf-8 -*-
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import xlrd
import os
import csv


datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"



def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(row, col) for col in range(sheet.ncols)]
                                         for row in range(sheet.nrows)]

    station = [str(e) for e in data[0][1:-1]]
    header = ["Station", "Year", "Month", "Day", "Hour", "Max Load"]
    result = []
    result.append(header)
    for e in range(len(station)):
        cost = sheet.col_values(e+1, start_rowx=1, end_rowx=None)
        maxvalue = max(cost)
        maxindex = cost.index(maxvalue) + 1
        maxresult = list(xlrd.xldate_as_tuple(data[maxindex][0], 0))[0:4]
        maxresult.insert(0, station[e])
        maxresult.append(maxvalue)
        result.append(maxresult)
    print result
    return result

def save_file(data, filename):
    # YOUR CODE HERE
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(data)

    csvfile.close()


def test():
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()
