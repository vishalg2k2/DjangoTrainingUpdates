from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Guide(models.Model):
    Area=models.CharField(max_length=50)
    Name=models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class Traveller(models.Model):
    Aadhar=models.CharField(max_length=16)
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=50)
    Phone=models.CharField(max_length=10)
    guide=models.ForeignKey(Guide,on_delete=models.SET_NULL,null=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    ighlighted = models.TextField()
    def __str__(self):
        return self.Name 


    

    