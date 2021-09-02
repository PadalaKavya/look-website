from django import forms
from django.forms import ModelForm
from .models import Articles,Challengers,Tasks, stressbusters,morning, workout,study, diet,skincare,night,detox


class ArtForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challengers
        fields = '__all__'


class TasksForms(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'

class StressForms(forms.ModelForm):
    class Meta:
        model = stressbusters
        fields = '__all__'

class morningform(forms.ModelForm):
    class Meta:
        model = morning
        fields = '__all__'

class workoutform(forms.ModelForm):
    class Meta:
        model = workout
        fields = '__all__'

class studyform(forms.ModelForm):
    class Meta:
        model = study
        fields = '__all__'

class dietform(forms.ModelForm):
    class Meta:
        model = diet
        fields = '__all__'

class skincareform(forms.ModelForm):
    class Meta:
        model = skincare
        fields = '__all__'

class nightform(forms.ModelForm):
    class Meta:
        model = night
        fields = '__all__'

class detoxform(forms.ModelForm):
    class Meta:
        model = detox
        fields = '__all__'
