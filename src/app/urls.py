from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .utils import generateString

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('request/', views.request, name = 'make request'),
    path('viewrequests/', views.viewrequests, name = 'view requests'),
    path('import/', views.importData, name = 'import data'),
    path('export/', views.exportData, name = 'export data'),
    path('faqs/', views.faqs, name = 'FAQs'),
    path('about/', views.about, name = 'About'),
    path('contacts/', views.contacts, name = 'Contacts'),
    path('rate/', views.rating, name = 'rate'),
    path('staff/export/download/', views.downloadFile, name='download'),
    path('staff/overview/', views.adminOverview, name ='admin overview'),
    path('staff/configure/request/timeout', views.adminTimeout, name = 'configure timeout'),
    path('staff/configure/request/allowance', views.requestAllowance, name = 'request allowance'),
    path('staff/configure/request/allowance/enable/duo', views.enableRequests, name = 'enable duo requests'),
    path('staff/configure/request/allowance/disable/duo', views.disableRequests, name = 'disable duo requests'),
    path('staff/configure/request/allowance/enable/single', views.enableSingleRequests, name = 'enable single requests'),
    path('staff/configure/request/allowance/disable/single', views.disableSingleRequests, name = 'disable single requests'),
    path('staff/configure/clean-database/confirm', views.cleanConfirmation, name = 'confirm clean'),
    path('staff/configure/clean/database', views.cleanData, name = 'clean data'),
    path('staff/match/make', views.match, name = 'make matches'),
    path('request/single', views.singleRequest, name = 'single request'),
    path(r'^request/confirm/(?P<ridb64>[0-9]{10})/(?P<token>[0-9]{10})/$', views.confirmRequest1, name = 'confirmRequest1'),
    path(r'^request/confirm/(?P<ridb64>[0-9]{10})/(?P<token>[0-9]{10}+)/$', views.confirmRequest2, name = 'confirmRequest2'),
    path(r'^request/confirm/(?P<id>[0-9]{10})/$', views.checkStatus, name = 'check status'),
    #path('debug/', views.debug, name = "debug"),
    #path(generateString() + '?P<ridb64>' + generateString() + '?P<token>' + generateString(), views.confirmRequest1, name = 'confirmRequest1'),
    #path(generateString() + '?P<ridb64>' + generateString() + '?P<token>' + generateString(), views.confirmRequest2, name = 'confirmRequest2'),
    #path(generateString() + '?P<id>' + generateString(), views.checkStatus, name = 'check status'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
