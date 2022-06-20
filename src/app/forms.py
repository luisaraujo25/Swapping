from django import forms
from .models import UC, Class, ClassUC
from .utils import *
from .settingsUtils import getTimeout


class RequestForm(forms.Form):
    email1 = forms.EmailField(required=True)
    email2 = forms.EmailField(required=True)
    uc = forms.ModelChoiceField(queryset=UC.objects.all(), required=True)
    #widget=ReadOnlyText SEE THIS
    class1 = forms.ModelChoiceField(
        queryset=Class.objects.all(), required=False, widget = forms.HiddenInput())
    class2 = forms.ModelChoiceField(
        queryset=Class.objects.all(), required=False, widget = forms.HiddenInput())


class ImportData(forms.Form):
    UCs = forms.FileField(required=False, label = "UCs (uc.csv)")
    Class = forms.FileField(required=False, label = "Classes (turmas.csv)")
    Students = forms.FileField(required=False, label = "Students ()")
    StudentUC = forms.FileField(required=False, label = "What UCs are students enrolled (colocacoes.csv)")
    Composed = forms.FileField(required=False, label = "Composed classes (compostos.csv)")
    ScheduleSlot = forms.FileField(required=False, label = "Schedules (horarios.csv)")


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


class ExportData(forms.Form):
    justChanges = forms.BooleanField(required=False)


class RatingForm(forms.Form):
    number = forms.ChoiceField(label = "Your Rating")
    opinion = forms.CharField(widget=forms.Textarea, required = False, label = "Leave something to justify your rating (not required)")

    def __init__(self, *args, **kwargs):

        numbers = (
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5")
        )
        super(RatingForm, self).__init__(*args, **kwargs)
        self.fields['number'].choices = numbers
        self.fields['number'].initial = 5


class SingleRequestForm(forms.Form):
    up = forms.IntegerField(label = "Your student number (up)")
    uc = forms.ModelChoiceField(queryset=UC.objects.all(), label = "UC:")
    cl = forms.ModelChoiceField(queryset=Class.objects.all(), label = "Desired class")
