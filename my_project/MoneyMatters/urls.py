from django.urls import path
from MoneyMatters import views

app_name = 'MoneyMatters'

urlpatterns = [
    path('',views.home,name = 'home'),
    path('Savings/',views.Sav,name= 'Savings'),
    path('Debts/',views.Debt,name= 'Debts'),
    path('MTG/', views.MT, name='MTG'),
    path('Expenses/', views.Expense, name='Expenses'),
    path('Income/', views.Inc, name='Income'),
    path('Delete/<str:pk>/', views.delete, name='Delete'),
    path('DDelete/<str:pk>/', views.ddelete, name='DDelete'),
    path('MDelete/<str:pk>/', views.mdelete, name='MDelete'),
    #path('EDelete/<str:pk>/', views.edelete, name='EDelete'),
    ]
