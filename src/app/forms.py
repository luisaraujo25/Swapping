from django import forms

class RequestForm(forms.Form):

    name = forms.CharField(label = 'nameField', max_length=60, required=True)
