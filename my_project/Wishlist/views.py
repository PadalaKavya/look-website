from django.shortcuts import render, redirect
from django.http import HttpResponse
from Wishlist.models import Wish
from Wishlist.forms import WishForms

# Create your views here.
def wishview(request):
    wishes = Wish.objects.all()
    form = WishForms()

    if request.method == "POST":
        form = WishForms(request.POST)
        if form.is_valid():
            form.save()


        else:
            print('Add Wishes')

    context = {'wishes':wishes, 'form':form}
    return render(request,'Wishlist/home_wish.html',context)

def CList(request):
    list = Wish.objects.all()
    list_dict =list.filter(catagory = 'Clothing')
    context = {'list':list_dict}
    return render(request,'Wishlist/clothing.html',context)

def Slist(request):
    stat = Wish.objects.all()
    list = stat.filter(catagory = 'Stationery')
    context = {'stat':list}
    return render(request,'Wishlist/Stationery.html',context)

def Ilist(request):
    stat = Wish.objects.all()
    list = stat.filter(catagory='Idea log')
    context = {'stat': list}
    return render(request, 'Wishlist/Idea.html', context)
def Tlist(request):
    stat = Wish.objects.all()
    list = stat.filter(catagory='Travel')
    context = {'stat': list}
    return render(request, 'Wishlist/Travel.html', context)

def Elist(request):
    stat = Wish.objects.all()
    list = stat.filter(catagory='Errands')
    context = {'stat': list}
    return render(request, 'Wishlist/Errands.html', context)
def Vlist(request):
    stat = Wish.objects.all()
    list = stat.filter(catagory='Souvenirs')
    context = {'stat': list}
    return render(request, 'Wishlist/Souv.html', context)
def Hlist(request):
    stat = Wish.objects.all()
    list = stat.filter(catagory='Health care')
    context = {'stat': list}
    return render(request, 'Wishlist/Health.html', context)
def Mlist(request):
    stat = Wish.objects.all()
    list = stat.filter(catagory='Shows/Movies')
    context = {'stat': list}
    return render(request, 'Wishlist/Movies.html', context)
def Blist(request):
    stat = Wish.objects.all()
    list = stat.filter(catagory='Books')
    context = {'stat': list}
    return render(request, 'Wishlist/Books.html', context)
def Edit(request, pk):
    uplist = Wish.objects.get(id=pk)
    form = WishForms(instance=uplist)
    if request.method == "POST":
        form = WishForms(request.POST, instance=uplist)
        if form.is_valid():
            form.save()
            return redirect('/Wishlist/List')

    context = {'form': form}
    return render(request, 'Wishlist/edit.html', context)

def delete(request, pk):
    note = Wish.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('/Wishlist/Wish')
    context = {'note': note}
    return render(request, 'Wishlist/delete.html', context)


def List(request):
    wishes = Wish.objects.all()
    wishes.order_by("catagory")
    context = {'wishes':wishes}
    return render(request, 'Wishlist/list.html', context)
