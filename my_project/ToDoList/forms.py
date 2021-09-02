from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput


from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'Deadline': DateInput(),
            'color': TextInput(attrs={'type': 'color'}),
        }
