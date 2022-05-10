import re
import datetime
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core import mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from .models import *

def validateEmail(mail):
    valid = re.search("^up[0-9]{9}@.+\.up\.pt$", mail)
    if valid == None:
        return -1


def getUp(mail):

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

    obj = ClassUC.objects.get(cl = cl, uc = uc)
    if obj == None:
        return False
    else:
        return True
    
def checkStudents(s1, s2):

    if s1 == s2:
        return False
    else:
        return True

def checkStudentUC(st, uc):
    obj = StudentUC.objects.get(student = st, uc = uc)
    if obj == None:
        return False
    else:
        return True

# def checkStudentClass(st,cl):
#     obj = StudentUC.objects.get(student = st,  = uc)
#     if obj == None:
#         return False
#     else:
#         return True

def validateRequest(email1, email2, cl1, cl2, uc, st1, st2):

    s1 = Student.objects.get(pk = st1)
    s2 = Student.objects.get(pk = st2)

    if validateEmail(email1) == -1 or validateEmail(email2) == -1:
        return -1
    if checkClassUC(cl1,uc) == False or checkClassUC(cl2,uc) == False:
        return -1
    if checkStudents(s1,s2) == False:
        return -1
    if checkStudentUC(s1, uc) == False or checkStudentUC(s2, uc) == False:
        return -1
    # if checkStudentClass(s1, cl1) == False or checkStudentClass(s2, cl2):
    #     return -1
    else:
        return 0