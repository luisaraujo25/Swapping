import re
import datetime
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core import mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes

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
    if s1.up == s2.up:
        return False
    else:
        return True

def checkStudentUC(st, uc):
    obj = StudentUC.objects.get(student = st, uc = uc)
    if obj == None:
        return False
    else:
        return True