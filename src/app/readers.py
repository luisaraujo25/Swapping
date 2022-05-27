import csv
from mimetypes import init
from operator import delitem

def readClasses(file):

    f = open(file,'r')
    
    reader = csv.DictReader(f, delimiter=';')
    
    classes = []
    for row in reader:
        classes.append(row['SIGLA'])
        
    f.close()

    return classes

def readUC(file):

    f = open(file, 'r', encoding = "ISO-8859-1")
    reader = csv.DictReader(f, delimiter=';')

    codes = []
    initials = []
    names = []

    for row in reader:
        codes.append(row['CODIGO'])
        initials.append(row['SIGLA'])
        names.append(row['NOME'])

    dict = {
        "codes": codes,
        "initials": initials,
        "names": names
    }

    return dict


def readClassUC(fileClasses):

    f = open(fileClasses, 'r')
    reader = csv.DictReader(f, delimiter=';')

    classUC = []
    for row in reader:
        elem = [row['CODIGO'], row['SIGLA']]
        classUC.append(elem)

    return classUC

def readStudents(file):

    f = open(file, 'r')
    reader = csv.DictReader(f, delimiter=';')
    
    students = []
    for row in reader:
        elem = [row['Numero'], row['Nome'], row['Email'], row['Sigla do curso']]
        students.append(elem)

    return students
    #suggestion: create dics and then list of dics

#MISSING STUDENT UC CLASS, schedule slot

#print(readStudents('../../exp/EstudantesL.EIC.csv'))

#print(readClasses("files/data.csv"))