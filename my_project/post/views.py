from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
#@login_required
def home(request):
    return render(request,'post/home.html')

class HomeView(ListView):
    model = BlogPost
    template_name = "post/home2.html"

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = BlogPost
    template_name = "post/article_details.html"
    context_object_name = 'post'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddPostView(LoginRequiredMixin,CreateView):
    model = BlogPost
    template_name = "post/add_post.html"
    #fields = '__all__'
    form_class = CreateBlogPostForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class DeletePostView(DeleteView):
    model = BlogPost
    template_name = "post/delete_post.html"
    success_url = reverse_lazy('post:home2')
class AddcommentView(LoginRequiredMixin,CreateView):
    model = comment
    form_class = EditComment
    template_name = "post/add_comment.html"
    #fields = '__all__'
    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.BlogPost_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('post:home2')

class your_post(ListView):
    model = BlogPost
    template_name = "post/users_post.html"
    context_object_name="academies"
    def get_queryset(self):
        return BlogPost.objects.filter(author = self.request.user)

"""things to be added:
1. self help articles
2. your friends posts -- everyones posts done
3. personal message the person
5. """
