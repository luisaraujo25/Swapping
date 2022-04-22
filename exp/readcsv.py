import csv

file = open('turmas.csv')

csvReader = csv.reader(file)

header = []
header = next(csvReader)
# header

rows = []
for row in csvReader:
    rows.append(row)
# rows

print(rows)

file.close()