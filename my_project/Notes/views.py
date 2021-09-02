from django.shortcuts import render, redirect
from django.http import HttpResponse
from Notes.models import Notes
from Notes.forms import NotesForms

def index(request):
    notes = Notes.objects.all()
    form = NotesForms()

    if request.method == "POST":
        form = NotesForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/Notes')

        else:
            print('Add notes')
    context = {'notes': notes, 'form': form}

    return render(request, 'Notes/notes.html', context)


def UpdateNotes(request, pk):
    upnotes = Notes.objects.get(id=pk)
    form = NotesForms(instance=upnotes)

    if request.method == "POST":
        form = NotesForms(request.POST, instance=upnotes)
        if form.is_valid():
            form.save()
            return redirect('/Notes')

    context = {'form': form}
    return render(request, 'Notes/updatenotes.html', context)


def delete(request, pk):
    note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/Notes')
    context = {'note': note}
    return render(request, 'Notes/delete.html', context)
