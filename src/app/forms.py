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
    Class = forms.FileField(help_text='max. 40 megabytes', required=False)
    ClassUC = forms.FileField(help_text='max. 40 megabytes', required=False)
    StudentUC = forms.FileField(help_text='max. 40 megabytes', required=False)
    ScheduleSlot = forms.FileField(help_text='max. 40 megabytes', required=False)
    Students = forms.FileField(help_text='max. 40 megabytes', required=False)
    UCs = forms.FileField(help_text='max. 40 megabytes', required=False)
