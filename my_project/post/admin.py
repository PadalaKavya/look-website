from django.contrib import admin
from post.models import BlogPost
from post.models import comment
admin.site.register(BlogPost)
admin.site.register(comment)
