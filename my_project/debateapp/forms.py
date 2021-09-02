from django.forms import ModelForm
from .models import Poll,textbox_model
from django import forms

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']
class EditTextbox(forms.ModelForm):
    class Meta:
        model = textbox_model
        fields = ('body',)
        widgets = {
        'body': forms.Textarea(attrs={'class':'form-control'}),
        }
