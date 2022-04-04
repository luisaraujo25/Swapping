from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('request', views.request, name = 'make request'),
    path('viewrequest/<int:idReq>/', views.viewrequest, name = 'view request')
]
