from django.db import models

# Create your models here.
class admin(models.Model):
    objects = None
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    USERNAME = models.CharField(max_length=50, blank=True)
    PASSWORD = models.CharField(max_length=50, blank=True)
class doctor(models.Model):
    objects = None
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    USERNAME = models.CharField(max_length=50, blank=True)
    PASSWORD = models.CharField(max_length=50, blank=True)
    DEPARTMENT = models.CharField(max_length=50, blank=True)
    MOBILE = models.CharField(max_length=50,blank=True)
    ADDRESS = models.CharField(max_length=50,blank=True)
    File = models.ImageField(upload_to='image/')
    status = models.CharField(max_length=50, blank=True,default="onhold")