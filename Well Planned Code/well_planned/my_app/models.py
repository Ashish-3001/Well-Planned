from django.db import models

# Create your models here.

class TodoListCatagory(models.Model):
    name = models.CharField(max_length=50) 

class DairyCatagory(models.Model):
    name = models.CharField(max_length=50)