from django.shortcuts import render, redirect
from .models import Articles,Challengers, Tasks, stressbusters, morning,workout,study,diet, skincare, night, detox
from .forms import ArtForm,ChallengeForm,TasksForms, StressForms, morningform,workoutform,studyform,dietform, skincareform, nightform, detoxform


# Create your views here.
def self(request):
    homep = {'home_insert': '<BR>'}
    return render(request, 'Selfcare/homepage.html', context=homep)

def articles(request):
    art = Articles.objects.all()
    context= {'art':art}
    return render(request, 'Selfcare/Articles.html', context)

def challenges(request):
    chal = Challengers.objects.all()
    context = {'chal':chal}
    return render(request, 'Selfcare/Challengers/Chp.html', context)

def ChalTasks(request,pk):
    chal = Challengers.objects.get(id=pk)
    tasks = Tasks.objects.all()
    context = {'tasks':tasks, 'chal':chal}
    return render(request,'Selfcare/Challengers/Tasks.html',context)

#stressbusters
def stressbuster(request):
    return render(request,'Selfcare/stressbuster/homepage.html')
def sbsessions(request):
    tasks = stressbusters.objects.all()
    context = {'tasks': tasks}
    return render(request, 'Selfcare/stressbuster/session.html', context=context)
def sbintro(request):
    return render(request,'Selfcare/stressbuster/intro.html')
def sbstep1(request):
    return render(request,'Selfcare/stressbuster/step1.html')
def sbstep2(request):
    return render(request,'Selfcare/stressbuster/step2.html')
def sbstep3(request):
    tasks = stressbusters.objects.all()
    form = StressForms()
    if request.method == "POST":
        form = StressForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Selfcare/stressbuster')
    context = {'tasks': tasks, 'form': form}
    return render(request,'Selfcare/stressbuster/step3.html',context=context)
def deletesb(request,pk):
    item = stressbusters.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/Selfcare/stressbuster')
    context = {'item':item}
    return render(request, 'Selfcare/stressbuster/delete.html',context)

#routine
def routines(request):
    return render(request,'Selfcare/routine/homepage.html')
def morningr (request):
    tasks = morning.objects.all()
    form = morningform()
    if request.method == "POST":
        form = morningform(request.POST)
        if form.is_valid():
            form.save()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'Selfcare/routine/morning.html',context=context)
def medit(request,pk):
    task = morning.objects.get(id=pk)
    form = morningform(instance=task)
    if request.method == 'POST':
        form = morningform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/Selfcare/mroutine')

    context = {'form': form}
    return render(request, 'Selfcare/routine/medit.html', context)
def workoutr (request):
    tasks = workout.objects.all()
    form = workoutform()
    if request.method == "POST":
        form = workoutform(request.POST)
        if form.is_valid():
            form.save()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'Selfcare/routine/workout.html',context=context)
def wedit(request,pk):
    task = workout.objects.get(id=pk)
    form = workoutform(instance=task)
    if request.method == 'POST':
        form = workoutform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/Selfcare/wroutine')

    context = {'form': form}
    return render(request, 'Selfcare/routine/wedit.html', context)
def studyr(request):
    tasks = study.objects.all()
    form = studyform()
    if request.method == "POST":
        form = studyform(request.POST)
        if form.is_valid():
            form.save()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'Selfcare/routine/study.html', context=context)
def sedit(request,pk):
    task = study.objects.get(id=pk)
    form = studyform(instance=task)
    if request.method == 'POST':
        form = studyform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/Selfcare/sroutine')

    context = {'form': form}
    return render(request, 'Selfcare/routine/sedit.html', context)
def dietr(request):
    tasks = diet.objects.all()
    form = dietform()
    if request.method == "POST":
        form = dietform(request.POST)
        if form.is_valid():
            form.save()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'Selfcare/routine/diet.html', context=context)
def dedit(request,pk):
    task = diet.objects.get(id=pk)
    form = dietform(instance=task)
    if request.method == 'POST':
        form = dietform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/Selfcare/droutine')

    context = {'form': form}
    return render(request, 'Selfcare/routine/dedit.html', context)
def skincarer(request):
    tasks = skincare.objects.all()
    form = skincareform()
    if request.method == "POST":
        form = skincareform(request.POST)
        if form.is_valid():
            form.save()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'Selfcare/routine/skincare.html', context=context)
def cedit(request,pk):
    task = skincare.objects.get(id=pk)
    form = skincareform(instance=task)
    if request.method == 'POST':
        form = skincareform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/Selfcare/croutine')

    context = {'form': form}
    return render(request, 'Selfcare/routine/cedit.html', context)
def nightr(request):
    tasks = night.objects.all()
    form = nightform()
    if request.method == "POST":
        form = nightform(request.POST)
        if form.is_valid():
            form.save()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'Selfcare/routine/night.html', context=context)
def nedit(request,pk):
    task = night.objects.get(id=pk)
    form = nightform(instance=task)
    if request.method == 'POST':
        form = nightform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/Selfcare/nroutine')

    context = {'form': form}
    return render(request, 'Selfcare/routine/nedit.html', context)
def detoxr(request):
    tasks = detox.objects.all()
    form = detoxform()
    if request.method == "POST":
        form = detoxform(request.POST)
        if form.is_valid():
            form.save()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'Selfcare/routine/detox.html', context=context)
def xedit(request,pk):
    task = detox.objects.get(id=pk)
    form = detoxform(instance=task)
    if request.method == 'POST':
        form = detoxform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/Selfcare/xroutine')

    context = {'form': form}
    return render(request, 'Selfcare/routine/xedit.html', context)
