from django.urls import path
from Wishlist import views

app_name = 'Wishlist'

urlpatterns = [
    path('Wish/', views.wishview, name='index'),
    path('Clothes/', views.CList, name='clothes'),
    path('Stationery/', views.Slist, name='stationery'),
    path('Idealog/', views.Ilist, name='Idealog'),
    path('Travel/', views.Tlist, name='Travel'),
    path('Errands/', views.Elist, name='Errands'),
    path('souv/', views.Vlist, name='souv'),
    path('health/', views.Hlist, name='health'),
    path('shows/', views.Mlist, name='shows'),
    path('books/', views.Blist, name='books'),
    path('Edit/<str:pk>/', views.Edit, name='Edit'),
    path('Delete/<str:pk>/', views.delete, name='Delete'),
    path('List/', views.List, name='list'),
]
