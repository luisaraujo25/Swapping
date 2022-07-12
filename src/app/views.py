from ast import Import
from bdb import effective
from django.forms import HiddenInput
from django.shortcuts import render
from django.http import *
from django.urls import reverse
from .models import *
from .forms import *
from .utils import *
from .ioFiles import *
from .settingsUtils import *
from .validators import *
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import os
import time

# Create your views here.

#Unlike other frameworks, a view function in Django takes a request and returns a response (action) - request handlers
#What the user sees is a template


def home(request):
    return render(request, 'home.html')


def request(request):

    enabled = getAllowance("duo")
    form = ""
    #If requests are enables
    if enabled == True:

        #form
        if request.method == 'POST':

            # create a form instance and populate it with data from the request:
            form = RequestForm(request.POST)
            # check whether it's valid:
            if form.is_valid():

                email1 = form.cleaned_data['email1']
                email2 = form.cleaned_data['email2']
                up1 = getUp(email1)
                up2 = getUp(email2)
                uc = form.cleaned_data['uc']

                st1 = None
                st2 = None
                class1 = None
                class2 = None
                
                valid = checkStudent(up1) & checkStudent(up2)
                if valid == True:
                    st1 = Student.objects.get(pk=up1)
                    st2 = Student.objects.get(pk=up2)
                else:
                    #request.method = 'GET'
                    message = "One or more invalid students"
                    return render(request, 'request.html', {'form': form, 'enabled': enabled, 'message' : message})

                valid = checkStudentUC(st1, uc) & checkStudentUC(st2,uc)
                if valid == True:
                    class1 = StudentUC.objects.get(uc = uc, student = st1).cl
                    class2 = StudentUC.objects.get(uc = uc, student = st2).cl
                else:
                    message = "One or more students aren't enrolled in this UC (neither a class)"
                    #request.method = 'GET'
                    return render(request, 'request.html', {'form': form, 'enabled': enabled, 'message' : message})

                message = validateRequest(email1, email2, class1, class2, uc, st1, st2)
                if message != "":
                    #request.method = 'GET'
                    return render(request, 'request.html', {'form': form, 'enabled': enabled, 'message' : message})

                else:
                    obj = Request()

                    #generate tokens
                    token1 = tokenGenerator(up1)

                    obj.st1ID = st1
                    obj.st2ID = st2
                    obj.uc = uc
                    obj.date = time.time()
                    obj.token1 = token1
                    obj.class1 = class1
                    obj.class2 = class2

                    #save obj in the db
                    obj.save()

                    sendEmail(request, st1, obj, token1, email1, True)
                    return HttpResponseRedirect('/')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = RequestForm()

    return render(request, 'request.html', {'form': form, 'enabled': enabled, 'message' : None})


def viewrequests(request):

    requests = Request.objects.all()
    if request.user.is_authenticated:
        return render(request, 'admin/viewrequests.html', {'requests': requests})
    else:
        return HttpResponse("You don't have the right access to this page.")


def importData(request):

    if request.user.is_authenticated:

        countFiles = 0
        if request.method == 'POST':
            form = ImportData(request.POST, request.FILES)
            if form.is_valid():

                try:
                    fileHandler(request.FILES['UCs'], "UC")
                    countFiles += 1
                except:
                    print("No UC")

                try:
                    fileHandler(request.FILES['Class'], "Class")
                    countFiles += 1
                except:
                    print("No Class")

                try:
                    fileHandler(request.FILES['Students'], "Student")
                    countFiles += 1
                except:
                    print("No Student")

                try:
                    fileHandler(request.FILES['StudentUC'], "StudentUC")
                    countFiles += 1
                except:
                    print("No StudentUC")

                try:
                    fileHandler(request.FILES['Composed'], "Composed")
                    countFiles += 1
                except:
                    print("No Composed")
                
                try:
                    fileHandler(request.FILES['ScheduleSlot'], "ScheduleSlot")
                    countFiles += 1
                except:
                    print("No ScheduleSlot")

                #request.method = 'GET'
                message = "uploaded " + str(countFiles) + " files!"
                return render(request, 'admin/import.html', {'form': form, 'message': message})
                #return HttpResponseRedirect('/staff/overview/')
        else:
            form = ImportData()
            
        return render(request, 'admin/import.html', {'form': form, 'message': None})

    else:
        return HttpResponse("You don't have the right access to this page.")


def exportData(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ExportData(request.POST)
            if form.is_valid():
                justChanges = form.cleaned_data['justChanges']
                generateFile(justChanges)
                return HttpResponseRedirect('/staff/export/download')
        else:
            form = ExportData()

        return render(request, 'admin/export.html', {'form': form})
    else:
        return HttpResponse("You don't have the right access to this page.")


def downloadFile(request):

    if request.user.is_authenticated:
        fileName = 'output.csv'
        dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = dir + "/app/files/" + fileName
        f = open(path, 'r')
        response = HttpResponse(f.read(), content_type="text/csv")
        response['Content-Disposition'] = "attachment; fileName=" + fileName
        return response
    else:
        return HttpResponse("You don't have the right access to this page.")


def confirmRequest1(request, ridb64, token):

    idRequest = force_bytes(urlsafe_base64_decode(ridb64))
    r = Request.objects.get(pk=idRequest)

    if r != None and token == r.token1:

        #do timeout if here
        timeNow = time.time()
        timeoutSeconds = getTimeout() * 60 * 60
        if timeNow - float(r.date) > timeoutSeconds:
            r.cancelled = True
            return HttpResponse("Timeout, two days have passed since this request was made, your response is no longer valid")
        else:
            r.confirmed1 = True
            st2 = r.st2ID
            token2 = tokenGenerator(st2.up)
            r.token2 = token2
            r.save()
            sendEmail(request, st2, r, token2, st2.email, False)
            return HttpResponse("Confirmed! Now sending email to the second Student")

    else:
        return HttpResponse("error")


def confirmRequest2(request, ridb64, token):

    idRequest = force_bytes(urlsafe_base64_decode(ridb64))
    r = Request.objects.get(pk=idRequest)

    if r != None and token == r.token2:

        #do timeout if here
        timeNow = time.time()
        timeoutSeconds = getTimeout() * 60*60
        if timeNow - float(r.date) > timeoutSeconds:
            r.cancelled = True
            return HttpResponse("Timeout, two days have passed since this request was made, your response is no longer valid")
        else:
            #CHANGE DATA
            r.confirmed2 = True
            r.save()
            cl1 = r.class1
            cl2 = r.class2
            st1 = r.st1ID
            st2 = r.st2ID
            uc = r.uc
            stClassUc1 = StudentUC.objects.get(cl=cl1, student=st1, uc=uc)
            stClassUc2 = StudentUC.objects.get(cl=cl2, student=st2, uc=uc)

            aux = stClassUc1.cl
            stClassUc1.cl = cl2
            stClassUc2.cl = aux

            stClassUc1.save()
            stClassUc2.save()
            return HttpResponse("Classes swapped!")
    else:
        return HttpResponse("Unable to conclude your request")


def faqs(request):
    return render(request, 'faqs.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')

def adminOverview(request):
    if request.user.is_authenticated:
        return render(request, 'admin/overview.html')
    else:
        return HttpResponse("You don't have the right access to this page.")


def adminTimeout(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
            form = ConfigureTimeout(request.POST)
            if form.is_valid():
                timeout = form.cleaned_data['timeout']
                setTimeout(timeout)
                return HttpResponseRedirect('/staff/configure/request/timeout')
        else:
            form = ConfigureTimeout()

        return render(request, 'admin/confTimeout.html', {'form': form})

    else:
        return HttpResponse("You don't have the right access to this page.")


def requestAllowance(request):

    if request.user.is_authenticated:

        duoOp = getAllowance("duo")
        singleOp = getAllowance("single")

        return render(request, 'admin/requestAllowance.html', {'duoOp': duoOp, 'singleOp': singleOp})

    else:
        return HttpResponse("You don't have the right access to this page.")


def enableRequests(request):

    if request.user.is_authenticated:
        setAllowance(True, "duo")
        return HttpResponseRedirect('/staff/configure/request/allowance')
    else:
        return HttpResponse("You don't have the right access to this page.")


def disableRequests(request):

    if request.user.is_authenticated:
        setAllowance(False, "duo")
        return HttpResponseRedirect('/staff/configure/request/allowance')
    else:
        return HttpResponse("You don't have the right access to this page.")

def enableSingleRequests(request):

    if request.user.is_authenticated:
        setAllowance(True, "single")
        return HttpResponseRedirect('/staff/configure/request/allowance')
    else:
        return HttpResponse("You don't have the right access to this page.")


def disableSingleRequests(request):

    if request.user.is_authenticated:
        setAllowance(False, "single")
        return HttpResponseRedirect('/staff/configure/request/allowance')
    else:
        return HttpResponse("You don't have the right access to this page.")



def checkStatus(request, id):

    try:
        req = Request.objects.get(pk=id)
        return render(request, 'status.html', {'req': req})

    except:
        return HttpResponse("Invalid link/this request doesn't exist")

def cleanData(request):

    if request.user.is_authenticated:
        ComposedClasses.objects.all().delete()
        StudentUC.objects.all().delete()
        ClassUC.objects.all().delete()
        Request.objects.all().delete()
        ScheduleSlot.objects.all().delete()
        Student.objects.all().delete()
        UC.objects.all().delete()
        Class.objects.all().delete()
        Composed.objects.all().delete()
        SingleRequest.objects.all().delete()
        
        return HttpResponseRedirect('/staff/overview/')

    else:
        return HttpResponse ("You don't have the right access to this page.")

def cleanConfirmation(request):

    if request.user.is_authenticated:
        return render(request, 'admin/cleanConfirm.html')
    else:
        return HttpResponse ("You don't have the right access to this page.")

def rating(request):

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            try:
                opinion = form.cleaned_data['opinion']
            except:
                opinion = ""
            Rating(number = number, opinion = opinion).save()
            
            message = "Thank you for your contribution."
            return render(request, 'rate.html', {'form': form, 'message': message})
    else:
        form = RatingForm()

    return render(request, 'rate.html', {'form': form, 'message': None})


def singleRequest(request):

    enabled = getAllowance("single")
    form = ""
    if enabled == True:

        if request.method == 'POST':
            form = SingleRequestForm(request.POST)

            if form.is_valid():
                up = form.cleaned_data['up']
                uc = form.cleaned_data['uc']
                cl = form.cleaned_data['cl']

                st = None

                valid = checkStudent(up)
                if valid:
                    st = Student.objects.get(pk=up)
                else:
                    message = "Invalid Student"
                    return render(request, 'singleRequest.html', {'form': form, 'enabled': enabled, 'message': message})

                valid = checkStudentUC(st, uc)
                if valid:
                    curCl = StudentUC.objects.get(uc=uc, student=st).cl
                else:
                    message = "You are not enrolled in this UC"
                    return render(request, 'singleRequest.html', {'form': form, 'enabled': enabled, 'message': message})

                valid = checkClassUC(cl, uc)
                if valid == False:
                    message = "This class doesn't exist in this UC"
                    return render(request, 'singleRequest.html', {'form': form, 'enabled': enabled, 'message': message})

                #desired class MUST be different than current class
                valid = checkStudentClassUC(st, cl, uc)
                if valid:
                    message = "Your desired class MUST be different than your current class"
                    return render(request, 'singleRequest.html', {'form': form, 'enabled': enabled, 'message': message})

                valid = checkSchedule(st, cl, uc)
                if valid == False:
                    message = "You can't go to this class since it overlaps your schedule."
                    return render(request, 'singleRequest.html', {'form': form, 'enabled': enabled, 'message': message})

                SingleRequest(st=st, uc=uc, desiredClass=cl).save()

                return HttpResponseRedirect('/')
        else:
            form = SingleRequestForm()

    return render(request, 'singleRequest.html', {'form': form, 'enabled': enabled, 'message' : None})


def match(request):

    matches = makeMatches()
    effectivateSingles(matches)

    return render(request, 'admin/matches.html', {'matches': matches})

def notFound(request, exception):
    
    return render(request, 'notFound.html')
