from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from time import time
from random import seed, randint, choice
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, punctuation


def generateString():

    url = ""
    seed(time())
    max_length = 30
    min_length = 20
    length = randint(min_length, max_length)

    for i in range(length):
        
        if i%2 or i%3:
            url += choice(ascii_letters)
        elif i%5:
            url += choice(digits)
        else:
            url += choice(punctuation)
            

    return url


urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('request/', views.request, name = 'make request'),
    path('viewrequests/', views.viewrequests, name = 'view requests'),
    path('import/', views.importData, name = 'import data'),
    path('export/', views.exportData, name = 'export data'),
    path('faqs/', views.faqs, name = 'FAQs'),
    path('about/', views.about, name = 'About'),
    path('contacts/', views.contacts, name = 'Contacts'),
    path('rate/', views.rating, name = 'Rate'),
    path('staff/export/download/', views.downloadFile, name='download'),
    path('staff/overview/', views.adminOverview, name ='admin overview'),
    path('staff/configure/request/timeout', views.adminTimeout, name = 'configure timeout'),
    path('staff/configure/request/allowance', views.requestAllowance, name = 'request allowance'),
    path('staff/configure/request/allowance/enable', views.enableRequests, name = 'enable requests'),
    path('staff/configure/request/allowance/disable', views.disableRequests, name = 'disable requests'),
    path('staff/configure/clean-database/confirm', views.cleanConfirmation, name = 'confirm clean'),
    path('staff/configure/clean/database', views.cleanData, name = 'clean data'),
    path('staff/match/make', views.match, name = 'make matches'),
    path('request/single', views.singleRequest, name = 'single request'),
    path(generateString() + '?P<ridb64>' + generateString() + '?P<token>' + generateString(), views.confirmRequest1, name = 'confirmRequest1'),
    path(generateString() + '?P<ridb64>' + generateString() + '?P<token>' + generateString(), views.confirmRequest2, name = 'confirmRequest2'),
    path(generateString() + '<int:id>' + generateString(), views.checkStatus, name = 'check status'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
