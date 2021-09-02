from django import forms
from django.forms import ModelForm
from .models import Wish


class WishForms(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ('wish','catagory',)
