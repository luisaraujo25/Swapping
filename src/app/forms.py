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
    file = forms.FileField(help_text='max. 40 megabytes')
    file2 = forms.FileField(help_text='max. 40 megabytes')
    file3 = forms.FileField(help_text='max. 40 megabytes')
    file4 = forms.FileField(help_text='max. 40 megabytes')
    file5 = forms.FileField(help_text='max. 40 megabytes')
    file6 = forms.FileField(help_text='max. 40 megabytes')
    