import csv
from os import remove

#remove dups (some files arent clean)
def removeDups(list):
    aux = []
    for i in list:
        if i not in aux:
            aux.append(i)

    return aux

def readClasses(file):

    f = open(file,'r')
    
    reader = csv.DictReader(f, delimiter=';')
    
    classes = []
    for row in reader:
        classes.append(row['SIGLA'])
        
    f.close()

    return removeDups(classes)

def readUC(file):

    f = open(file, 'r', encoding = "ISO-8859-1")
    reader = csv.DictReader(f, delimiter=';')

    ucs = []

    for row in reader:
        elem = {
            "code": row['CODIGO'],
            "initials": row['SIGLA'],
            "name": row['NOME']
        }
        ucs.append(elem)

    return removeDups(ucs)


def readClassUC(fileClasses):

    f = open(fileClasses, 'r')
    reader = csv.DictReader(f, delimiter=';')

    classUC = []
    for row in reader:
        elem = {
            "uc": row['CODIGO'],
            "cl": row['SIGLA']
        }
        classUC.append(elem)

    return removeDups(classUC)

def readStudents(file):

    f = open(file, 'r')
    reader = csv.DictReader(f, delimiter=';')
    
    students = []
    for row in reader:
        elem = {
            "up": row['Numero'],
            "name": row['Nome'],
            "email": row['Email'],
            "course": row['Sigla do curso']
        }
        students.append(elem)

    return removeDups(students)

def readStudentUC(file):
    f = open(file, 'r')
    reader = csv.DictReader(f, delimiter=';')

    list = []
    for row in reader:
        elem = {
            "up": row['ESTUDANTE'],
            "uc": row['UC'],
            "class": row['TURMA']
        }
        list.append(elem)

    return removeDups(list)

#MISSING STUDENT UC CLASS, schedule slot

#print(readStudents('../../exp/EstudantesL.EIC.csv'))

#print(readClasses("files/data.csv"))

#print(readClassUC('../../exp/turmas.csv'))