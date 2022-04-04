from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('request/', views.request, name = 'make request'),
    path('viewrequest/<int:idReq>/', views.viewrequest, name = 'view request'),
    path('import/', views.importData, name = 'import data'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]
