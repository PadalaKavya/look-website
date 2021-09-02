from basicapp import views
from django.urls import path
app_name = 'basicapp'
urlpatterns = [
      path('',views.index,name='index'),
      path('register/',views.register,name='register'),
      path('user_login/',views.user_login,name="user_login"),
      #path('logout/',views.user_logout,name='logout')
]
