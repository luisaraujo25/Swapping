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

#print(rows)

file.close()


def getCourse(classCode):

    course = ""
    for i in classCode:
        if i.isnumeric():
            continue
        else:
            course += i

    print(course)
    return course

def getNumber(classCode):
    
    number = ""
    first = True
    for i in classCode:
        if first:
            first = False
            continue
        
        if i.isnumeric() == False:
            continue
        else:
            number += i

    return int(number)

getCourse("1LEIC06")
print(getNumber("1LEIC06"))
