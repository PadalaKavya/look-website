from django import forms
from django.forms import ModelForm
from .models import Savings, Debts, MTG, Expenses, Income

class SavingForm(forms.ModelForm):
    class Meta:
        model = Savings
        fields = ('title','amount',)

class DebtForm(forms.ModelForm):
    class Meta:
        model = Debts
        fields = ('title','amount','due')

class MTGForm(forms.ModelForm):
    class Meta:
        model = MTG
        fields = ('title','amount',)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ('title','amount',)

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'
