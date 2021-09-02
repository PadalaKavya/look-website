from django.db import models

# Create your models here.
catagory_choices = [('Shows/Movies', 'Shows/Movies'),('Books', 'Books'),('Stationery', 'Stationery'), ('Clothing', 'Clothing'),
                    ('Idea log', 'Idea log'), ('Health care', 'Health care'), ('Travel', 'Travel'),
                    ('Errands', 'Errands'), ('Souvenirs', 'Souvenirs'), ]
class Wish(models.Model):
    wish = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    catagory = models.CharField(max_length=20, choices= catagory_choices,default='Errands')

    def __str__(self):
        return self.wish
