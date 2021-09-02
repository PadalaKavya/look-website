from django.shortcuts import render, redirect
from .models import Vision,Milestone
from .forms import VisionForm, MileForm

def Board(request):
    go = Vision.objects.all()
    form = VisionForm()

    if request.method == "POST":
        form = VisionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/VisionBoard')

        else:
            print('Add goals')
    context = {'go': go, 'form': form}

    return render(request, 'VisionBoard/Vision.html', context)

def deletevis(request,pk):
    item = Vision.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/VisionBoard')

    context = {'item':item}
    return render(request, 'VisionBoard/deletev.html',context)

def Milestones(request):
    target = Milestone.objects.all()
    form = MileForm()
    if request.method == 'POST':
        form = MileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/VisionBoard/Milestones')

    context = {'target':target,'form': form}
    return render(request, 'VisionBoard/goal.html', context)

def updateMilestone(request, pk):
    target = Milestone.objects.get(id=pk)
    form = MileForm(instance=target)
    if request.method == 'POST':
        form = MileForm(request.POST,instance=target)
        if form.is_valid():
            form.save()
            return redirect('/VisionBoard/Milestones')

    context = {'form':form}
    return render(request,'VisionBoard/updatemile.html',context)

def deleteMile(request,pk):
    item = Milestone.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/VisionBoard/Milestones')

    context = {'item':item}
    return render(request, 'VisionBoard/delete.html',context)
