from django import forms

class RequestForm(forms.Form):

    name = forms.CharField(max_length=60, required=True)
    email1 = forms.EmailField(required=True)
    email2 = forms.EmailField(required=True)
    uc = forms.CharField(max_length=60, required=True)
    class1 = forms.IntegerField(required=True)
    class2 = forms.IntegerField(required=True)