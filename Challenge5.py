import csv
with open ('Names.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)