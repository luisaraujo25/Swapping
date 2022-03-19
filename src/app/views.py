from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Unlike other frameworks, a view function in Django takes a request and returns a response (action) - request handlers
#What the user sees is a template

def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'home.html', {'var': 'passei uma variavel'})