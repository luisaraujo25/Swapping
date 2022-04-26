import re
from django.core.mail import send_mail


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

def sendEmail(email):
    send_mail(
    'Class Exchange Request',
    'Troca de turma.',
    'swappingfeup@gmail.com',
    [email],
    fail_silently=False,
)

sendEmail("qfrabray300@gmail.com")