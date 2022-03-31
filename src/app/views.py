from django.shortcuts import render
from django.http import HttpResponse
from .models import UC
# Create your views here.

#Unlike other frameworks, a view function in Django takes a request and returns a response (action) - request handlers
#What the user sees is a template

def home(request):
    # return HttpResponse("Hello World")

    # b = UC(name="ESOF")
    # b.save()
    b = UC.objects.create(name='test')
    b.save()
    data = UC.objects.all()
    return render(request, 'home.html', data)

def request(request):
    return render(request,'request.html')