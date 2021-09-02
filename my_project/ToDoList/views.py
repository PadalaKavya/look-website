from django.shortcuts import render,redirect
from ToDoList.models import Task
from ToDoList.forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/ToDoList')

    context = {'tasks': tasks, 'form':form}
    return render(request, 'ToDoList/list.html', context)



def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/ToDoList')

    context = {'form':form}
    return render(request,'ToDoList/update_task.html',context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/ToDoList')

    context = {'item':item}
    return render(request, 'ToDoList/delete.html',context)
