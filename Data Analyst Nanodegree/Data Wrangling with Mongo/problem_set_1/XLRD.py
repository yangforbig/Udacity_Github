import xlrd
datafile = '2013_ERCOT_Hourly_Load_Data.xls'

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    # include header
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col)
                for col in range(sheet.ncols)]
                    for r in range(sheet.nrows)]

    print "\nList Comprehension"
    print "data[3][2]:"
    print data[3][2]
    print data[0][0]
    print type(sheet)
    '''
    print "\nCells in a nested loop:"
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print sheet.cell_value(row, col)

    print 'Number of rows in the sheet:'
    print sheet.nrows
    print "Type of data in cell(row, 3 col 2):"
    print sheet.cell_type(3,2)
    print "Value in cell(row 3, col 2):",
    print sheet.cell_value(3,2)
    print "Get a slice of values in column 3, from rows 1-3"
    print sheet.col_values(3, start_rowx=1, end_rowx=4)

    print "\nDate:"
    print "TYpe of data in cell (row1, col 0):"
    print sheet.cell_type(1,0)
    exceltime = sheet.cell_value(1,0)
    print "Time in Excel format:",
    print sheet.cell_type()
    print "Convert time to a Python datatime tuple, from the Excel float"
    #print xlrd.xldate_as_tuple(exceltime, 0)
    '''

    cost = sheet.col_values(1, start_rowx=1, end_rowx=None)
    maxvalue = max(cost)
    minvalue = min(cost)
    maxindex = cost.index(maxvalue) + 1
    minindex = cost.index(minvalue) + 1
    maxtime = xlrd.xldate_as_tuple(data[maxindex][0], 0)
    mintime = xlrd.xldate_as_tuple(data[minindex][0], 0)
    result = {
               "maxvalue": maxvalue,
               "minvalue": minvalue,
               "maxtime": maxtime,
               "mintime": mintime,
    }
    print result
    return data

data = parse_file(datafile)
