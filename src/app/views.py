from django.shortcuts import render
from django.http import *
from .models import *
from .forms import *
from .utils import *
from datetime import datetime

# Create your views here.

#Unlike other frameworks, a view function in Django takes a request and returns a response (action) - request handlers
#What the user sees is a template

def home(request):
    # return HttpResponse("Hello World")

    # b = UC(name="ESOF")
    # b.save()
    # b = UC.objects.create(name='test')
    # b.save()
    # data = UC.objects.all()
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

            if validateEmail(email1) == -1 or validateEmail(email2) == -1:
                return HttpResponse("Invalid email(s)")

            else:
                obj = Request()
                up1 = getUp(email1) 
                up2 = getUp(email2)
                obj.st1ID = Student.objects.get(pk=up1)
                obj.st2ID = Student.objects.get(pk=up2)
                obj.confirmed1 = False
                obj.confirmed2 = False
                # obj.date = datetime.now()
                obj.uc = uc
                obj.class1 = class1
                obj.class2 = class2

                #save obj in the db
                obj.save()

                return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestForm()

    return render(request, 'request.html', {'form': form})

def viewrequest(request, idReq):

    try:
        requests = SwapRequest.objects.get(id = idReq)
        date = requests.date
    except SwapRequest.DoesNotExist:
        raise Http404("Request does not exist")

    return render(request, 'viewrequest.html', {'id': idReq, 'date': date})

def importData(request):

    return render(request, 'import.html')