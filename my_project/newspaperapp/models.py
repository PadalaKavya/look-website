from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Category(models.Model):
    title=models.CharField(max_length = 200)
    category_image = models.ImageField(upload_to="imgs")
    def __str__(self):
        return self.title
class News(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length = 50 , null=False,blank=False)
    date_published = models.DateTimeField(auto_now_add=True)
    #details = models.TextField()
    details = RichTextUploadingField(blank=True,null= True)
    slug = models.SlugField(blank=True,unique=True)
    def slug(self):
        return slugify(self.date_published)
    def __str__(self):
        return self.title
