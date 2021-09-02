from django.urls import path
from . import views

app_name = 'Selfcare'

urlpatterns = [
    path('',views.self,name= 'home'),
    path('articles/', views.articles,name='articles'),
    path('challengers/', views.challenges, name='challengers'),
    path('<int:pk>/', views.ChalTasks, name='tasks'),
    #stressbusters
    path('stressbuster/', views.stressbuster, name='stressbuster'),
    path('intro/', views.sbintro, name='intro'),
    path('step1/', views.sbstep1, name='step1'),
    path('step2/', views.sbstep2, name='step2'),
    path('step3/', views.sbstep3, name='step3'),
    path('sessions/', views.sbsessions, name='sessions'),
    path('delete/<str:pk>/', views.deletesb, name="delete"),
    path('routine/', views.routines, name='routine'),
    path('mroutine/', views.morningr, name='mroutine'),
    path('medit/<str:pk>/', views.medit, name='medit'),
    path('wroutine/', views.workoutr, name='wroutine'),
    path('wedit/<str:pk>/', views.wedit, name='wedit'),
    path('sroutine/', views.studyr, name='sroutine'),
    path('sedit/<str:pk>/', views.sedit, name='sedit'),
    path('droutine/', views.dietr, name='droutine'),
    path('dedit/<str:pk>/', views.dedit, name='dedit'),
    path('croutine/', views.skincarer, name='croutine'),
    path('cedit/<str:pk>/', views.dedit, name='cedit'),
    path('nroutine/', views.nightr, name='nroutine'),
    path('nedit/<str:pk>/', views.nedit, name='nedit'),
    path('xroutine/', views.detoxr, name='xroutine'),
    path('xedit/<str:pk>/', views.xedit, name='xedit'),
]
