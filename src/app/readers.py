import csv
from os import remove

from app.models import Class, Composed, ComposedClasses
from app.utils import getClassesFromComp

#remove dups (some files arent clean)
def removeDups(list):
    aux = []
    for i in list:
        if i not in aux:
            aux.append(i)

    return aux


def sortCriteria(elem):
    return elem['up']


def readClasses(file):

    f = open(file, 'r')

    reader = csv.DictReader(f, delimiter=';')

    classes = []
    for row in reader:
        classes.append(row['SIGLA'])

    f.close()

    return removeDups(classes)


def readUC(file):

    f = open(file, 'r', encoding="ISO-8859-1")
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


def readClassUC(file):

    f = open(file, 'r')
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

    students.sort(key=sortCriteria, reverse=True)
    return removeDups(students)


def readStudentUC(file):
    f = open(file, 'r')
    reader = csv.DictReader(f, delimiter=';')

    list = []
    for row in reader:
        elem = {
            "up": row['ESTUD_NUM_UNICO_INST'],
            "uc": row['CODIGO'],
            "class": row['SIGLA']
        }
        list.append(elem)

    return removeDups(list)


def readComposed(file):
    f = open(file, 'r')
    reader = csv.DictReader(f, delimiter=';')

    list = []
    for row in reader:
        elem = {
            "compName": row['SIGLA'],
            "class": row['SIGLA_1']
        }
        list.append(elem)

    return removeDups(list)


def readSchedules(file):
    f = open(file, 'r')
    reader = csv.DictReader(f, delimiter=';')

    list = []
    for row in reader:

        type = row['TIPO_AULA']
        start = int(row['HORA_INICIO'])
        end = start + int(row['DURACAO'])
        cl = row['SIGLA']
        uc = row['CODIGO']
        weekDay = row['DECODE']
        
        #ignoring theoretical classes
        if type == 'T':
            continue

        elem = {}
        
        if "COMP" in cl:
            compClasses = getClassesFromComp(cl)
            for c in compClasses:
                elem = {
                    "class": c,
                    "uc": uc,
                    "weekDay": weekDay,
                    "start": start,
                    "end": end,
                    "type": type
                }
        else:
            elem = {
                "class": cl,
                "uc": uc,
                "weekDay": weekDay,
                "start": start,
                "end": end,
                "type": type
            }

        list.append(elem)

    return removeDups(list)
    
# schedule slot

#print(readStudents('../../exp/EstudantesL.EIC.csv'))

#print(readClasses("files/data.csv"))

#print(readClassUC('../../exp/turmas.csv'))
