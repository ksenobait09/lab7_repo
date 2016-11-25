from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    description = models.CharField(max_length=225)
    class Meta:
        db_table = 'Books'
