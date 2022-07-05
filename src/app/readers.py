import csv
from app.utils import getClassesFromComp, toFloat
from django.http import HttpResponse

#remove dups (some files arent clean)
def removeDups(list):
    aux = []
    for i in list:
        if i not in aux:
            aux.append(i)

    return aux

def cleanFiles(list):

    cleanedList = []

    list = removeDups(list)

    for obj in list:
    
        try:
            code = obj['CODIGO']
            int(code)
        except:
            cleanedList.append(obj)
    
    return cleanedList


def sortCriteria(elem):
    return elem['up']


def readClasses(file):

    f = open(file, 'r')

    reader = csv.DictReader(f, delimiter=';')

    reader = cleanFiles(reader)

    classes = []
    for row in reader:
        classes.append(row['SIGLA'])

    f.close()

    return classes


def readUC(file):

    f = open(file, 'r', encoding="ISO-8859-1")
    reader = csv.DictReader(f, delimiter=';')

    ucs = []

    reader = cleanFiles(reader)

    for row in reader:
        elem = {
            "code": row['CODIGO'],
            "initials": row['SIGLA'],
            "name": row['NOME']
        }
        ucs.append(elem)


    return ucs


def readClassUC(file):

    f = open(file, 'r')
    reader = csv.DictReader(f, delimiter=';')

    reader = cleanFiles(reader)

    classUC = []
    for row in reader:
        elem = {
            "uc": row['CODIGO'],
            "cl": row['SIGLA']
        }
        classUC.append(elem)

    return classUC


def readStudents(file):

    f = open(file, 'r', encoding="ISO-8859-1")
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

    reader = cleanFiles(reader)

    debug = open('app/files/import/debug.txt', 'w+')
    list = []
    for row in reader:

        type = row['TIPO_AULA']
        start = toFloat(row['HORA_INICIO'])
        dur = toFloat(row['DURACAO'])
        cl = row['SIGLA']
        uc = row['CODIGO']
        weekDay = row['DECODE(A.DIA_N,2,\'seg\',3,\'ter\',4,\'qua\',5,\'qui\',6,\'sex\')']
        
        #ignoring theoretical classes
        if type == 'T':
            continue
        
        if "COMP" in cl:
            compClasses = getClassesFromComp(cl)
            for c in compClasses:
                debug.write("comp: " + cl + ", class: " + c + "\n")
                elem = {
                    "class": c,
                    "uc": uc,
                    "weekDay": weekDay,
                    "start": start,
                    "dur": dur,
                    "type": type
                }
                list.append(elem)
        else:
            elem = {
                "class": cl,
                "uc": uc,
                "weekDay": weekDay,
                "start": start,
                "dur": dur,
                "type": type
            }
            list.append(elem)

    
    import json
    for i in removeDups(list):
        debug.write(json.dumps(i) + "\n")

    return list
    
# schedule slot

#print(readStudents('../../exp/EstudantesL.EIC.csv'))

#print(readClasses("files/data.csv"))

#print(readClassUC('../../exp/turmas.csv'))
