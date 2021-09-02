from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class BlogPost(models.Model):
    title = models.CharField(max_length = 50 , null=False,blank=False)
    #body = models.TextField(max_length = 5000 , null=False,blank=False)
    body = RichTextUploadingField(blank=True,null= True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #slug = models.SlugField(blank=True,unique=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:article-detail', args=(self.id,))

class comment(models.Model):
    BlogPost = models.ForeignKey(BlogPost,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)
    body = models.TextField(max_length = 5000)
    date_added = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User,on_delete=models.CASCADE)
    author = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return '%s  %s' % (self.BlogPost.title, self.name)
