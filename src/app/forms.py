from django import forms
from .models import UC, Class, ClassUC
from .utils import *

class RequestForm(forms.Form):
    email1 = forms.EmailField(required=True)
    email2 = forms.EmailField(required=True)
    uc = forms.ModelChoiceField(queryset = UC.objects.all(), required=True)
    class1 = forms.ModelChoiceField(queryset = Class.objects.all(), required=True)
    class2 = forms.ModelChoiceField(queryset = Class.objects.all(), required=True)
    
    #def __init__(self, *args, **kwargs):
    #    self.


class ImportData(forms.Form):
    Class = forms.FileField(required=False)
    ClassUC = forms.FileField(required=False)
    StudentUC = forms.FileField(required=False)
    ScheduleSlot = forms.FileField(required=False)
    Students = forms.FileField(required=False)
    UCs = forms.FileField(required=False)


class ConfigureTimeout(forms.Form):

    timeout = forms.ChoiceField()

    def __init__(self, *args, **kwargs):

        hours = (
            (1, "1h"),
            (2, "2h"),
            (4, "4h"),
            (8, "8h"),
            (12, "12h"),
            (24, "24h"),
            (48, "48h"),
            (72, "72h")
        )
        super(ConfigureTimeout, self).__init__(*args, **kwargs)
        self.fields['timeout'].choices = hours
        self.fields['timeout'].initial = getTimeout()
