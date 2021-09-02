from django import forms
from django.forms import ModelForm
from .models import Notes


class NotesForms(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('text',)
