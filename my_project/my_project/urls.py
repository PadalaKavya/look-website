
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from basicapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('basicapp/',include('basicapp.urls')),
    path('logout/',views.user_logout,name='logout'),
    path("newspaperapp/",include("newspaperapp.urls")),
    path("debateapp/",include("debateapp.urls")),
    path("post/",include("post.urls")),
    path('ckeditor/',include('ckeditor_uploader.urls')),
     path('Homepage/', include('Homepage.urls')),
    path('Selfcare/',include('Selfcare.urls')),
    path('Notes/', include('Notes.urls')),
    path('Wishlist/', include('Wishlist.urls')),
    path('ToDoList/',include('ToDoList.urls')),
    path('MoneyMatters/',include('MoneyMatters.urls')),
    path('VisionBoard/',include('VisionBoard.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
