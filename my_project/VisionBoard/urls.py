from django.urls import path
from . import views

app_name = 'VisionBoard'

urlpatterns = [
    path('', views.Board, name="VisionBoard"),
    path('Milestones/', views.Milestones, name="Milestones"),
    path('updatemile/<str:pk>/', views.updateMilestone, name= "updatemile"),
    path('delete/<str:pk>/', views.deleteMile, name="delete"),
    path('deletev/<str:pk>/', views.deletevis, name="deletev"),
]
