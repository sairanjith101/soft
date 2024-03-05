from django.db import models

# Create your models here.

class Student(models.Model):
    Sno = models.IntegerField()
    Sname = models.CharField(max_length = 30)
    Sclass = models.IntegerField()
    Saddress = models.CharField(max_length = 50)
