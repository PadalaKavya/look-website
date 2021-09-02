from post import views
from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,AddcommentView,DeletePostView,your_post

app_name = 'post'
urlpatterns = [
             path('',HomeView.as_view(),name = "home2"),
             path('your_post',your_post.as_view(),name = "your_post"),
             path('article/<int:pk>',ArticleDetailView.as_view(),name = "article-detail"),
             path('add_post/',AddPostView.as_view(),name="add_post"),
             path('article/<int:pk>/comment',AddcommentView.as_view(),name="add_comment"),
             path('article/<int:pk>/delete',DeletePostView.as_view(),name = "delete_post"),
]
