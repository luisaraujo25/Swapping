import datetime
from django.utils.http import urlsafe_base64_encode
from django.core import mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from .models import Composed, ComposedClasses

def getUp(mail):

    if mail == "lmpa.pt@gmail.com":
        return 201904995
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


def getCourse(classCode):

    course = ""
    for i in classCode:
        if i.isnumeric():
            continue
        else:
            course += i

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


def getClassesFromComp(compName):

    comp = Composed.objects.get(name = compName)
    listComposedClasses = ComposedClasses.objects.filter(composed = comp)
    listClasses = [x.cl.code for x in listComposedClasses] 
    return listClasses

def toFloat(string):
    return float(string.replace(',','.'))