from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100, unique=True)
    address = models.TextField(null=True)
    contact_no = models.IntegerField(null=True)
    job_title = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=100,null=True)
    password1 =  models.CharField(max_length=100,null=True)
    password2 =  models.CharField(max_length=100,null=True)

class Analyst(models.Model):
    name = models.CharField(max_length=100, primary_key  = True)
    company = models.CharField(max_length=200)

class Assets(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    inception_date = models.DateTimeField(default=timezone.now)
    isActive = models.BooleanField()
    analyst = models.ForeignKey(Analyst, on_delete=models.CASCADE)


    
