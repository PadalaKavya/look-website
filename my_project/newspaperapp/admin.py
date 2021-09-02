from django.contrib import admin

# Register your models here.
from .models import Category,News
admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display=('title','category')

admin.site.register(News,AdminNews)
