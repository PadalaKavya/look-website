from django.urls import path
app_name = 'newspaperapp'
from django.conf import settings
from . import views
from .views import SearchView
urlpatterns=[
path('',views.home,name='home'),
path('results/', SearchView.as_view(), name='search'),
path('results/detail/<int:id>',views.detail,name='detail'),
path('category/<int:id>',views.category,name='category'),
]
