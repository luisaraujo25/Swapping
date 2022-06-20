from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('request/', views.request, name = 'make request'),
    path('viewrequest/<int:idReq>/', views.viewrequest, name = 'view request'),
    path('viewrequests/', views.viewrequests, name = 'view requests'),
    path('import/', views.importData, name = 'import data'),
    path('export/', views.exportData, name = 'export data'),
    path('faqs/', views.faqs, name = 'FAQs'),
    path('about/', views.about, name = 'About'),
    path('contacts/', views.contacts, name = 'Contacts'),
    path('staff/export/download/', views.downloadFile, name='download'),
    path('staff/overview/', views.adminOverview, name ='admin overview'),
    path('staff/configure/request/timeout', views.adminTimeout, name = 'configure timeout'),
    path('staff/configure/request/allowance', views.requestAllowance, name = 'request allowance'),
    path('staff/configure/request/allowance/enable', views.enableRequests, name = 'enable requests'),
    path('staff/configure/request/allowance/disable', views.disableRequests, name = 'disable requests'),
    path('staff/configure/clean/database', views.cleanData, name = 'clean data'),
    path(r'^confirm/first/(?P<ridb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]*{1,20})/$', views.confirmRequest1, name = 'confirmRequest1'),
    path(r'^confirm/second/(?P<ridb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]*{1,20})/$', views.confirmRequest2, name = 'confirmRequest2'),
    path('request/status/Arfghkrlkl$W%/lk396w0jas<int:id>jndhys8g782/', views.checkStatus, name = 'check status'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
