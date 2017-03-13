import csv

# Define data
data = [(1, "A towel,", 1.0),
        (42, " it says, ", 2.0),
        (1337, "is about the most ", -1),
        (0, "massively useful thing ", 123),
        (-2, "an interstellar hitchhiker can have.", 3)]

# Write CSV file
with open('test.csv', 'w') as fp:
    writer = csv.writer(fp, delimiter=',')
    for row in data:
        writer.writerow(data)
