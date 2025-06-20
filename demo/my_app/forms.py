from django import forms
from django.forms import DateInput
from my_app.models import ApplicationModel


class ApplicationForms(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = ('__all__')
        widgets = {'preferred_start_date': DateInput(attrs={'type': 'date'}),}