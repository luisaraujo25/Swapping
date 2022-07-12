import datetime
from django.utils.http import urlsafe_base64_encode
from django.core import mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from .models import Composed, ComposedClasses, SingleRequest, StudentUC
from time import time
from random import seed, randint, choice
from string import ascii_letters, digits, punctuation


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

def flattenList(list):
    return [x for xs in list for x in xs]

def hadPermission(request):
    if request.user.is_authenticated:
        return True
    return False

def makeMatches():

    debug = open('app/files/debug/matching.txt', 'w+')

    requests = list(SingleRequest.objects.filter(closed = False))

    #brute force for now
    matches = []
    for i in range(len(requests)):
        request1 = requests[i]
        curClass1 = StudentUC.objects.get(student = request1.st, uc = request1.uc).cl
        debug.write("i: " + request1.st.name + ", " + curClass1.code + "\n")
        for j in range(len(requests)):
            if i == j:
                continue
            request2 = requests[j]
            curClass2 = StudentUC.objects.get(student = request2.st, uc = request2.uc).cl

            if curClass1 == request2.desiredClass and curClass2 == request1.desiredClass:
                if [request1,request2] not in matches and [request2,request1] not in matches:
                    debug.write(request1.st.name + " + " + request2.st.name + "\n")
                    tuple = [request1, request2]
                    matches.append(tuple)

    return matches

def effectivateSingles(matches):

    debug = open('app/files/debug/effectivate.txt', 'w+')

    for tuple in matches:

        request1 = tuple[0]
        request2 = tuple[1]

        request1.closed = True
        request2.closed = True

        request1.save()
        request2.save()

        stUc1 = StudentUC.objects.get(student = request1.st, uc = request1.uc)
        stUc2 =  StudentUC.objects.get(student = request2.st, uc = request2.uc)

        aux = stUc1.cl
        stUc1.cl = stUc2.cl
        stUc1.save()

        stUc2.cl = aux
        stUc2.save()

        debug.write(stUc1.student.name + " - " + stUc1.cl.code + "\n")
        debug.write(stUc2.student.name + " - " + stUc2.cl.code + "\n")
        

def generateString():

    url = ""
    seed(time())
    max_length = 30
    min_length = 20
    length = randint(min_length, max_length)

    for i in range(length):
        
        if i%2 or i%3:
            url += choice(ascii_letters)
        elif i%5:
            url += choice(digits)
        else:
            url += choice(punctuation)
            

    return url
