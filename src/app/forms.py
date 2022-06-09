from django import forms
from .models import UC, Class, ClassUC
from .utils import *

class RequestForm(forms.Form):
    email1 = forms.EmailField(required=True)
    email2 = forms.EmailField(required=True)
    uc = forms.ModelChoiceField(queryset = UC.objects.all(), required=True)
    class1 = forms.ModelChoiceField(queryset = Class.objects.all(), required=True)
    class2 = forms.ModelChoiceField(queryset = Class.objects.all(), required=True)
    
class ImportData(forms.Form):
    Class = forms.FileField(required=False)
    ClassUC = forms.FileField(required=False)
    StudentUC = forms.FileField(required=False)
    ScheduleSlot = forms.FileField(required=False)
    Students = forms.FileField(required=False)
    UCs = forms.FileField(required=False)

class Login(forms.Form):
    email = forms.EmailField(required = True)
    password = forms.PasswordInput