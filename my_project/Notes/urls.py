from django.urls import path
from Notes import views

app_name = 'Notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('updatenotes/<str:pk>/', views.UpdateNotes, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]
