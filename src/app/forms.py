from django import forms
from .models import UC, Class

class RequestForm(forms.Form):

    name = forms.CharField(max_length=60, required=True)
    email1 = forms.EmailField(required=True)
    email2 = forms.EmailField(required=True)
    uc = forms.ModelChoiceField(queryset = UC.objects.all(), required=True )
    class1 = forms.ModelChoiceField(queryset = Class.objects.all(), required=True)
    class2 = forms.ModelChoiceField(queryset = Class.objects.all(), required=True)
