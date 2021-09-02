from django import forms
from django.forms import ModelForm
from .models import Vision,Milestone

class VisionForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = '__all__'

class MileForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = '__all__'
