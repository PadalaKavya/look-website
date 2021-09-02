from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.
class Vision(models.Model):
    goal = models.CharField(blank=True, null=True, max_length=200)
    icon = RichTextUploadingField(blank=True, null=True)
    @property
    def __str__(self):
        return self.goal

class Milestone(models.Model):
    milestones = RichTextField(max_length=250,default='Write What you want to achieve:'
                                           'Little steps that take you towards achieving your goal.')
    complete = models.BooleanField(default=False)
    @property
    def __str__(self):
        return self.milestones
