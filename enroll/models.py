from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
