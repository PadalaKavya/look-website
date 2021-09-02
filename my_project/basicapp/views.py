from django.shortcuts import render
from . import forms
from basicapp.forms import UserForm,UserProfileInfoForm
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
import re
from django.contrib.auth import get_user_model
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')
#there is a special function written here
"""def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")"""


@login_required
def user_logout(request):
    logout(request)
    #returns to homepage
    return HttpResponseRedirect(reverse('basicapp:index'))

def register(request):


    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            #hash the password
            user.set_password(user.password)
            #update the password
            user.save()

            profile=profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()


            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basicapp/registration.html',
                             {'user_form': user_form,
                              'profile_form':profile_form,
                              'registered':registered})


User = get_user_model()

class UsernameOrEmailBackend(ModelBackend):

    def authenticate(self,request, username=None, password=None,**kwargs):
        if '@' in username:
            kwargs = {'email': username}
        elif re.search("^0?[5-9]{1}\d{9}$",username):   #optional
            kwargs = {'phone_no':username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



def user_login(request):

    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        """user = User.objects.create_user(username=post_data['email'])
        user.username = post_data['email']
        user.save()"""
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('basicapp:index'))
                #HttpResponse('you are logged in')

            else:
                return HttpResponse('account not active')
        else:
            print("someone tried to login and failed!")
            print('username: {} and password {}' .format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'basicapp/login.html',{})
