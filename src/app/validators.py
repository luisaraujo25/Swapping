from .models import *


def validateEmail(mail):
    return True
    valid = re.search("^up[0-9]{9}@.+\.up\.pt$", mail)
    if valid == None:
        return False
    return True


def checkClassUC(cl, uc):

    try:
        ClassUC.objects.get(cl=cl, uc=uc)
        return True
    except:
        return False


def checkStudents(s1, s2):

    if s1 == s2:
        return False
    else:
        return True


def checkStudentUC(st, uc):

    try:
        StudentUC.objects.get(student=st, uc=uc)
        return True
    except:
        return False


def checkClass(cl1, cl2):
    if cl1 == cl2:
        return False
    else:
        return True


def checkStudent(st):
    try:
        Student.objects.get(pk=st)
        return True
    except:
        return False


def checkStudentClassUC(st, cl, uc):
    try:
        StudentUC.objects.get(student=st, cl=cl, uc=uc)
        return True
    except:
        return False


""" def checkSchedule(cl1, cl2):
    try:
        slot1 = ScheduleSlot()
    except:
        return False

 """


def validateRequest(email1, email2, cl1, cl2, uc, st1, st2):

    if validateEmail(email1) == False or validateEmail(email2) == False:
        return -1
    if checkStudent(st1) == False or checkStudent(st2) == False:
        return -1
    if checkClassUC(cl1, uc) == False or checkClassUC(cl2, uc) == False:
        return -1
    if checkStudents(st1, st2) == False:
        return -1
    if checkStudentUC(st1, uc) == False or checkStudentUC(st2, uc) == False:
        return -1
    if checkClass(cl1, cl2) == False:
        return -1
    if checkStudentClassUC(st1, cl1, uc) == False or checkStudentClassUC(st2, cl2, uc) == False:
            return -1
    else:
        return 0
