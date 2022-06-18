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
    #return HttpResponse(obj)
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
        for i in classUC:
            try:
                uc = UC.objects.get(code = i['uc'])
                cl = Class.objects.get(code = i['cl'])
                ClassUC(uc = uc, cl = cl).save()
            except:
                HttpResponse("there is not a class or uc associated")

    elif obj == "StudentUC":
        StudentUC.objects.all().delete()
        list = readStudentUC(path)
        for i in list:
            try:
                uc = UC.objects.get(code = i['uc'])
                cl = Class.objects.get(code = i['class'])
                st = Student.objects.get(up = i['up'])
                StudentUC(student = st, uc = uc, cl = cl).save()
            except:
                HttpResponse("student is not in the class X of uc Y")

    #elif obj == "ScheduleSlot":

    elif obj == "Composed":
        Composed.objects.all().delete()
        ComposedClasses.objects.all().delete()
        composed = readComposed(path)
        
        for i in composed:
            try:
                compObj = Composed.objects.get(name = i['compName'])
            except:
                compObj = Composed(name = i['compName'])
                compObj.save()
            classObj = Class.objects.get(code = i['class'])
            ComposedClasses(composed = compObj, cl = classObj).save()
            
    elif obj == "Student":
        Student.objects.all().delete()
        students = readStudents(path)
        for i in students:
            Student(up = i['up'], name = i['name'], email = i['email'], course = i['course']).save()

    elif obj == "UC":
        UC.objects.all().delete()
        ucs = readUC(path)
        for i in ucs:
            UC(code = i['code'], initials = i['initials'], name = i['name']).save()


def generateFile(justChanges):
    
    #check which requests are concluded
    f = open('app/files/output.csv', 'w')

    writer = csv.writer(f, delimiter=';')
    header = ['ESTUD_NUM_UNICO_INST', 'CODIGO', 'SIGLA']
    writer.writerow(header)

    if justChanges:
        changes = Request.objects.filter(confirmed1 = True, confirmed2 = True)
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