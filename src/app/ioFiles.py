from .models import *
from .readers import *
from django.http import HttpResponse
from .utils import *


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
        ClassUC.objects.all().delete()
        classes = readClasses(path)
        classUC = readClassUC(path)
        aux = []
        for i in classes:
            course = getCourse(i)
            no = getNumber(i)
            if i not in aux:
                Class(number=no, course=course, code=i).save()
                aux.append(i)
        
        for i in classUC:
            uc = UC.objects.get(code=i['uc'])
            cl = Class.objects.get(code=i['cl'])
            ClassUC(uc=uc, cl=cl).save()
        
    elif obj == "Student":
        Student.objects.all().delete()
        students = readStudents(path)
        for i in students:
            Student(up=i['up'], name=i['name'],
                    email=i['email'], course=i['course']).save()

    elif obj == "UC":
        UC.objects.all().delete()
        ucs = readUC(path)
        for i in ucs:
            UC(code=i['code'], initials=i['initials'], name=i['name']).save()
    
    elif obj == "StudentUC":
        StudentUC.objects.all().delete()
        list = readStudentUC(path)
        print(str(len(list)))
        for i in list:
            try:
                uc = UC.objects.get(code=i['uc'])
                cl = Class.objects.get(code=i['class'])
                st = Student.objects.get(up=i['up'])
                StudentUC(student=st, uc=uc, cl=cl).save()
            except:
                print("student doesnt exist in the database")

    elif obj == "ScheduleSlot":
        ScheduleSlot.objects.all().delete()
        slots = readSchedules(path)
        debug = open('app/files/debug2.txt','w+')
        #debug.write("en")
        for i in slots:

            cl = Class.objects.get(code = i['class'])
            uc = UC.objects.get(code = i['uc'])
            debug.write("class: " + cl.code + ", uc: " + uc.initials + "\n")
            try:
                clUc = ClassUC.objects.get(uc = uc, cl = cl)
                ss = ScheduleSlot(classUC = clUc, weekDay = i['weekDay'], startTime = i['start'], duration = i['dur'], typeClass = i['type'])
                ss.save()
                debug.write("class from schedule: " + ss.classUC.cl.code + ", uc from schedule: " + ss.classUC.uc.initials + "\n")

            except:
                continue
            
            #    print("Incoherent data")

    elif obj == "Composed":
        Composed.objects.all().delete()
        ComposedClasses.objects.all().delete()
        composed = readComposed(path)

        for i in composed:
            try:
                comp = Composed.objects.get(name=i['compName'])
            except:
                comp = Composed(name=i['compName'])
                comp.save()
            cl = Class.objects.get(code=i['class'])
            ComposedClasses(composed=comp, cl=cl).save()



def generateFile(justChanges):

    #check which requests are concluded
    f = open('app/files/output.csv', 'w+')

    writer = csv.writer(f, delimiter=';')
    header = ['ESTUD_NUM_UNICO_INST', 'CODIGO', 'SIGLA']
    writer.writerow(header)

    if justChanges:
        changes = Request.objects.filter(confirmed1=True, confirmed2=True)
        for elem in changes:
            data = [elem.st1ID.up, elem.uc.code, elem.class2.code]
            data2 = [elem.st2ID.up, elem.uc.code, elem.class1.code]
            writer.writerow(data)
            writer.writerow(data2)
    else:
        list = StudentUC.objects.all()
        for i in list:
            data = [i.student.up, i.uc.code, i.cl.code]
            writer.writerow(data)

    f.close()
