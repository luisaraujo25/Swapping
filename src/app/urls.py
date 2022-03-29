from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('request', views.request)
]
