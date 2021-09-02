from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

# Create your models here.
class Notes(models.Model):
    text = RichTextField(blank=True, null=True)
    #text = models.TextField()
    date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.text
