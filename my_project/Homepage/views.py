from django.shortcuts import render
# Create your views here.
def home(request):
    homep = {'home_insert':'<BR>'}
    return render(request,'Homepage/homepage.html',context=homep)
