from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True)
    about = models.TextField(blank=True)

class Book(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(blank=True)
    about = models.TextField(blank=True)



