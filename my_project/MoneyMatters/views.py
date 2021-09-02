
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Savings, Debts,MTG, Expenses, Income
from .forms import SavingForm, DebtForm,MTGForm, ExpenseForm, IncomeForm
from django.db.models import F,Sum
# Create your views here.
def home(request):
    homep = {'home_insert': '<BR>'}
    return render(request, 'MoneyMatters/home_money.html', context=homep)

def Sav(request):
    goal = Savings.objects.all()
    gform = SavingForm()

    if request.method == "POST":
        gform = SavingForm(request.POST)

        if gform.is_valid():
            gform.save()
    total = Savings.objects.aggregate(Sum('amount'))['amount__sum'] or 0.00
    context = {'goal': goal, 'gform': gform,'total':total}
    return render(request, 'MoneyMatters/Savings.html', context)
def delete(request, pk):
    note = Savings.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/MoneyMatters/Savings')
    context = {'note': note}
    return render(request, 'MoneyMatters/delete.html', context)

def Debt(request):
    debt = Debts.objects.all()
    dform = DebtForm()

    if request.method == "POST":
        dform = DebtForm(request.POST)

        if dform.is_valid():
            dform.save()
    total = Debts.objects.aggregate(Sum('amount'))['amount__sum'] or 0.00
    context = {'debt': debt, 'dform': dform,'total':total}
    return render(request, 'MoneyMatters/Debts.html', context)
def ddelete(request, pk):
    note = Debts.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/MoneyMatters/Debts')
    context = {'note': note}
    return render(request, 'MoneyMatters/ddelete.html', context)


def MT(request):
    mt = MTG.objects.all()
    mform = MTGForm()

    if request.method == "POST":
        mform = MTGForm(request.POST)

        if mform.is_valid():
            mform.save()
    total = MTG.objects.aggregate(Sum('amount'))['amount__sum'] or 0.00
    context = {'mt': mt, 'mform': mform,'total':total}
    return render(request, 'MoneyMatters/MTG.html', context)
def mdelete(request, pk):
    note = MTG.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/MoneyMatters/MTG')
    context = {'note': note}
    return render(request, 'MoneyMatters/mdelete.html', context)

def Expense(request):
    exp = Expenses.objects.all()
    eform = ExpenseForm()
    if request.method == "POST":
        eform = ExpenseForm(request.POST)
        if eform.is_valid():
            eform.save()

    total =Expenses.objects.aggregate(Sum('amount'))['amount__sum'] or 0.00
    context = {'exp':exp, 'eform':eform, 'total':total}
    return render(request, 'MoneyMatters/EXB.html',context)
"""def edelete(request,pk):
    note = Expenses.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/MoneyMatters/Expenses')
    context = {'note': note}
    return render(request, 'MoneyMatters/edelete.html', context)"""

def Inc(request):
    inc =Income.objects.all()
    iform = IncomeForm()
    if request.method == "POST":
        iform = IncomeForm(request.POST)
        if iform.is_valid():
            iform.save()

    itotal = Income.objects.aggregate(Sum('income'))['income__sum'] or 0.00
    etotal = Expenses.objects.aggregate(Sum('amount'))['amount__sum'] or 0.00
    total = itotal-etotal
    context = {'inc':inc, 'iform':iform, 'itotal':itotal, 'total':total}
    return render(request,'MoneyMatters/IYW.html',context)
