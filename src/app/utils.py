import re
import csv
import datetime
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core import mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from .models import *
from .readers import *

def validateEmail(mail):
    valid = re.search("^up[0-9]{9}@.+\.up\.pt$", mail)
    if valid == None:
        return False
    return True


def getUp(mail):

    #if mail == "lmpa.pt@gmail.com":
    #    return 201904995
    up = ""
    for i in mail:
        if i == 'u' or i == 'p':
            continue
        elif i == '@':
            break
        up = up + i
    
    return int(up)


def tokenGenerator(id):
    token = str(id) + str(datetime.datetime.now().timestamp())
    return token

def sendEmail(r, user, request, token, email, first):

    site = get_current_site(r)
    subject = 'Confirm your request'
    message = render_to_string('email.html', {
        'user': user,
        'domain': site.domain,
        'rid': urlsafe_base64_encode(force_bytes(request.id)),
        'tokenV': token,
        'first': first,
    })
    
    email = mail.EmailMessage(
        subject, message, to=[email]
    )
    connection = mail.get_connection()
    connection.open()
    email.send()
    connection.close()

def checkClassUC(cl, uc):

    try:
        ClassUC.objects.get(cl = cl, uc = uc)
    except:
        return False

    return True

def checkStudents(s1, s2):

    if s1 == s2:
        return False
    else:
        return True

def checkStudentUC(st, uc):

    try:
        StudentUC.objects.get(student = st, uc = uc)
    except:
        return False
    return True

def checkClass(cl1,cl2):
    if cl1 == cl2:
        return False
    else:
        return True

def checkStudent(st):
    try:
        Student.objects.get(pk = st)
    except:
        return False
    return True

def checkStudentClassUC(st,cl,uc):
    try:
        StudentUC.objects.get(student = st, cl = cl, uc = uc)
    except:
        return False
    return True

def validateRequest(email1, email2, cl1, cl2, uc, st1, st2):

    
    if validateEmail(email1) == False or validateEmail(email2) == False:
        return -1
    if checkStudent(st1) == False or checkStudent(st2) == False:
        return -1
    if checkClassUC(cl1,uc) == False or checkClassUC(cl2,uc) == False:
        return -1
    if checkStudents(st1,st2) == False:
        return -1
    if checkStudentUC(st1, uc) == False or checkStudentUC(st2, uc) == False:
        return -1
    if checkClass(cl1, cl2) == False:
        return -1
    if checkStudentClassUC(st1, cl1, uc) == False or checkStudentClassUC(st2, cl2, uc) == False:
        return -1
    else:
        return 0


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


def fileHandler(file, obj):
    f = open('app/files/data.csv', 'wb+')
    for info in file.chunks():
        f.write(info)
    f.close()
    saveImports(obj)
    
def saveImports(obj):    

    path = "app/files/data.csv"

    if obj == "Class":
        Class.objects.all().delete()
        classes = readClasses(path)
        aux = []
        for cl in classes:
            course = getCourse(cl)
            no = getNumber(cl)
            if cl not in aux:
                Class(number = no, course = course, code = cl).save()
                aux.append(cl)

    elif obj == "ClassUC":
        ClassUC.objects.all().delete()
        classUC = readClassUC(path)

    #elif obj == "StudentUC":

    #elif obj == "Schedule Slot":

    elif obj == "Student":
        Student.objects.all().delete()
        students = readStudents(path)

    elif obj == "UC":
        UC.objects.all().delete()
        ucs = readUC(path)
