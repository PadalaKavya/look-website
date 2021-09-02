from django.urls import path
from . import views

app_name = 'ToDoList'

urlpatterns =[
    path('',views.index, name ="list"),
    path('update_task/<str:pk>/', views.updateTask,name = "update_task"),
    path('delete/<str:pk>/', views.deleteTask,name = "delete"),
]
