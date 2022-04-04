from django.shortcuts import render
from django.http import HttpResponse
from .models import *
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
    return render(request,'request.html')

def viewrequest(request, idReq):

    try:
        requests = SwapRequest.objects.get(id = idReq)
        date = requests.date
    except SwapRequest.DoesNotExist:
        raise Http404("Request does not exist")

    return render(request, 'viewrequest.html', {'id': idReq, 'date': date})