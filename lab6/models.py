from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    description = models.CharField(max_length=225)
    class Meta:
        db_table = 'Books'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('name', 'author', 'description', 'NEW')
    list_display = ('name', 'author', 'description', 'NEW')
    search_fields = ('name', 'author')
    def NEW(self, obj):
        return 'new'

class signupModel(models.Model):
    name = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    description = models.CharField(max_length=225)