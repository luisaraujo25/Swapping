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


def checkSchedule(st, cl, uc):
    
    try:
        studentUcs = StudentUC.objects.filter(student = st)
        schedule = []
        #students whole practical schedule except the class to verify
        for stUc in studentUcs:
            stCl = stUc.cl 
            stUc = stUc.uc
            if stUc.code == uc:
                continue
            clUc = ClassUC.objects.get(cl = stCl, uc = stUc)
            slot = ScheduleSlot.objects.filter(classUC = clUc, typeClass = 'P')
            schedule.append(slot)

        #make sure there aren't lists of lists
        schedule = [x for xs in schedule for x in xs]

        clUc = ClassUC.objects.get(uc = uc, cl = cl)
        slot = ScheduleSlot.objects.filter(classUC = clUc, typeClass = 'P')
        st = Student.objects.get(up = st)

        valid = False
        for practical in schedule:
            if practical.weekDay == slot.weekDay and (practical.start + practical.duration <= slot.start or practical.start >= slot.start + slot.duration):
                #didn't have anything else to write lol, if i did the condition "backwards" it would be more extense
                valid = True
            else:
                print("debug")
                return False
        return True
    except:
        return False


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
    if checkStudentClassUC(st1, cl2, uc) == False or checkStudentClassUC(st2, cl2, uc) == False:
            return -1
    if checkSchedule(st2, cl1, uc) == False or checkSchedule(st2, cl2, uc) == False:
        return -1
    else:
        return 0
