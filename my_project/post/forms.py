from django import forms
from django.forms import ModelForm
from .models import *

class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','body']

class EditComment(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('body',)
        #fields = ('name','body')
        widgets = {
        #'name': forms.TextInput(attrs={'class':'form-control'}),
        'body': forms.Textarea(attrs={'class':'form-control'}),
        }
