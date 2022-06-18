from app.utils import flattenList
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


def checkSchedule(st, classToChange, uc):
    
    #DEBUG
        debug = open('app/files/debug.txt', 'w+')
    #try:
        studentUcs = list(StudentUC.objects.filter(student = st))
        schedule = []

        debug.write(str(len(studentUcs)))
        for i in studentUcs:
            debug.write(i.uc.initials + "\n\n")

        #students whole practical schedule except the class to verify
        for stUc in studentUcs:

            if stUc.uc == uc:
                continue
            clUc = ClassUC.objects.get(cl = stUc.cl, uc = stUc.uc)
            slot = list(ScheduleSlot.objects.filter(classUC = clUc, typeClass = 'PL'))
            for i in slot:
                debug.write(i.classUC.uc.initials + "\n")
            slot2 = list(ScheduleSlot.objects.filter(classUC = clUc, typeClass = 'TP'))
            for i in slot2:
                debug.write(i.classUC.uc.initials + "\n")
            
            schedule.append(slot)
            schedule.append(slot2)

        #make sure there aren't lists of lists

        clUc = ClassUC.objects.get(uc = uc, cl = classToChange)
        slot = list(ScheduleSlot.objects.filter(classUC = clUc, typeClass = 'PL')) + list(ScheduleSlot.objects.filter(classUC = clUc, typeClass = 'TP'))

        try:
            schedule = flattenList(schedule)
            slot = flattenList(slot + slot2)
        except:
            debug.write("nothing\n")

        valid = False
        for practical in schedule:
            debug.write(str(len(schedule)) + "\n")
            debug.write(practical.classUC.uc.initials + "\n")
            for sl in slot:
                debug.write("IM SLOT: " + sl.classUC.uc.initials + "\n")
                if practical.weekDay == sl.weekDay:
                    debug.write("here again\n")
                    if practical.startTime + practical.duration <= sl.startTime or practical.startTime >= sl.startTime + sl.duration:
                        #didn't have anything else to write lol, if i did the condition "backwards" it would be more extense
                        valid = True
                        debug.write("aqui")
                    else:
                        #DEBUG
                        debug.write("not valid")
                        return False
                else:
                    continue    
        return True
    #except:
    #    return False


def validateRequest(email1, email2, cl1, cl2, uc, st1, st2):

    if validateEmail(email1) == False or validateEmail(email2) == False:
        return -1
    #if checkStudent(st1) == False or checkStudent(st2) == False:
    #    return -1
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
    if checkSchedule(st1, cl2, uc) == False or checkSchedule(st2, cl1, uc) == False:
        return -1
    else:
        return 0
