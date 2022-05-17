from ast import Import
from django.shortcuts import render
from django.http import *
from .models import *
from .forms import *
from .utils import *
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

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
            # return HttpResponse(up2)
            if validateRequest(email1, email2, class1, class2, uc, up1, up2) == -1:
                return HttpResponse("Invalid Request")

            else:
                obj = Request()

                #generate tokens
                token1 = tokenGenerator(up1)

                obj.st1ID = Student.objects.get(pk=up1)
                obj.st2ID = Student.objects.get(pk=up2)
                # obj.date = datetime.now()
                obj.uc = uc
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

    return render(request, 'viewrequests.html', {'requests': requests})

def viewrequest(request, idReq):

    try:
        requests = Request.objects.get(id = idReq)
        date = requests.date
    except Request.DoesNotExist:
        raise Http404("Request does not exist")

    return render(request, 'viewrequest.html', {'id': idReq, 'date': date})


def importData(request):

    if request.method == 'POST':
        form = ImportData(request.POST, request.FILES)
        if form.is_valid():
            # fileHandler(request.FILES['file'])
            fileHandler(request.FILES['file'])
            return HttpResponse("uploaded")
    else:
        form = ImportData()
    
    return render(request, 'import.html', {'form': form})


def confirmRequest1(request, ridb64, token):
    
    idRequest = force_bytes(urlsafe_base64_decode(ridb64))
    r = Request.objects.get(pk = idRequest)

    if r != None and token == r.token1:

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
        #CHANGE DATA
        r.confirmed2 = True
        r.save()
        return HttpResponse("Classes swapped!")
    else:
        return HttpResponse("Unable to conclude your request")

def faqs(request):
    return render(request, 'faqs.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')