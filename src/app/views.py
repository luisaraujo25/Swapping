from ast import Import
from django.shortcuts import render
from django.http import *
from django.urls import reverse
from .models import *
from .forms import *
from .utils import *
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import os
import time

# Create your views here.

#Unlike other frameworks, a view function in Django takes a request and returns a response (action) - request handlers
#What the user sees is a template

def home(request):
    return render(request, 'home.html')


def request(request):

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = RequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            email1 = form.cleaned_data['email1']
            email2 = form.cleaned_data['email2']
            uc = form.cleaned_data['uc']
            class1 = form.cleaned_data['class1']
            class2 = form.cleaned_data['class2']
            up1 = getUp(email1) 
            up2 = getUp(email2)
            #return HttpResponse(up2)
            if validateRequest(email1, email2, class1, class2, uc, up1, up2) == -1:
                return HttpResponse("Invalid Request")

            else:
                obj = Request()

                #generate tokens
                token1 = tokenGenerator(up1)

                obj.st1ID = Student.objects.get(pk=up1)
                obj.st2ID = Student.objects.get(pk=up2)
                obj.uc = uc
                obj.date = time.time()
                obj.token1 = token1
                obj.class1 = class1
                obj.class2 = class2

                #save obj in the db
                obj.save()

                sendEmail(request, Student.objects.get(pk=up1), obj, token1, email1, True)

                return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestForm()

    return render(request, 'request.html', {'form': form})

def viewrequests(request):

    requests = Request.objects.all()
    if request.user.is_authenticated:
        return render(request, 'admin/viewrequests.html', {'requests': requests})
    else:
        return HttpResponse("You don't have the right access to this page.")

def viewrequest(request, idReq):

    if request.user.is_authenticated:
        try:
            req = Request.objects.get(id = idReq)
            date = req.date
            return render(request, 'viewrequest.html', {'id': idReq, 'date': date})
        except Request.DoesNotExist:
            raise Http404("Request does not exist")
    
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
                    fileHandler(request.FILES['ClassUC'], "ClassUC")
                    countFiles += 1
                except:
                    print("No ClassUC")

                try:
                    fileHandler(request.FILES['StudentUC'], "StudentUC")
                    countFiles += 1
                except:
                    print("No StudentUC")

                try:
                    fileHandler(request.FILES['ScheduleSlot'], "ScheduleSlot")
                    countFiles += 1
                except:
                    print("No ScheduleSlot")

                try:
                    fileHandler(request.FILES['Students'], "Student")
                    countFiles += 1
                except:
                    print("No Student")

                return HttpResponse("uploaded " + str(countFiles) + " files!")
        else:
            form = ImportData()
        
        return render(request, 'admin/import.html', {'form': form})
    
    else:
        return HttpResponse("You don't have the right access to this page.")

def exportData(request):

    if request.user.is_authenticated:
        file = generateFile()
        return render(request, 'admin/export.html')
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
    r = Request.objects.get(pk = idRequest)

    if r != None and token == r.token1:

        #do timeout if here
        timeNow = time.time()
        timeoutSeconds = getTimeout() * 60 * 60
        if timeNow - r.date > timeoutSeconds:
            return HttpResponse("Timeout, two days have passed since this request was made, your response is no longer valid")
        else:
            r.confirmed1 = True
            st2 = r.st2ID
            token2 = tokenGenerator(st2.up)
            r.token2 = token2
            r.save()
            sendEmail(request, st2, r, token2, st2.email, False)
            return HttpResponse("confirmed")
        
    else:
        return HttpResponse("error")
        


def confirmRequest2(request, ridb64, token):
    
    idRequest = force_bytes(urlsafe_base64_decode(ridb64))
    r = Request.objects.get(pk = idRequest)
    
    if r != None and token == r.token2:

        #do timeout if here
        timeNow = time.time()
        timeoutSeconds = getTimeout() * 60*60
        if timeNow - r.date > timeoutSeconds:
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
            stClassUc1 = StudentUC.objects.get(cl = cl1, student = st1, uc = uc)
            stClassUc2 = StudentUC.objects.get(cl = cl2, student = st2, uc = uc)

            stClassUc1.cl = cl2
            stClassUc2.cl = cl1

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
                writeTimeout(timeout)
                return HttpResponseRedirect('/staff/configure/timeout')
        else:
            form = ConfigureTimeout()
        
        return render(request, 'admin/confTimeout.html', {'form': form})
    
    else:
        return HttpResponse("You don't have the right access to this page.")

