from django.db import models
# import os
from twilio.rest import Client

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
class patient_tb(models.Model):
    objects = None
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    Date = models.DateTimeField('Created',auto_now=True)
    patient_id = models.IntegerField(default=0)
    USERNAME = models.CharField(max_length=50, blank=True)
    PASSWORD = models.CharField(max_length=50, blank=True)
    DOCTOR_DEPARTMENT = models.CharField(max_length=50, blank=True)
    MOBILE = models.CharField(max_length=50, blank=True)
    ADDRESS = models.CharField(max_length=50, blank=True)
    Symptoms = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, blank=True, default="onhold")

class book_appointment(models.Model):
    objects = None
    Name= models.CharField(max_length=50, blank=True)
    patient_id = models.IntegerField(default=0)
    Date= models.DateTimeField('Created',auto_now=True)
    Description = models.CharField(max_length=50, blank=True)
    Doctor_Department = models.CharField(max_length=50,blank=True)
    USERNAME =  models.CharField(max_length=50,blank=True)
    MOBILE = models.CharField(max_length=50,blank=True)
    ADDRESS = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True, default="onhold")

class discharge_tb(models.Model):
    objects = None
    p_id = models.ForeignKey(patient_tb,on_delete=models.CASCADE)
    Patient_username = models.CharField(max_length=50, blank=True)
    patient_id = models.IntegerField(default=0)
    Doctor_username = models.CharField(max_length=50,blank=True)
    Release_date = models.DateTimeField('Created', auto_now=True)
    Room_charge = models.IntegerField(default=0)
    Doc_fee = models.IntegerField(default=0)
    Medicine_cost = models.ImageField(default=0)
    Other_charge = models.IntegerField(default=0)
    Total_charge = models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        if self.Total_charge>0:
            account_sid = 'ACb734174b9d7deb5783d172d041e9806b'
            auth_token = 'fd21aabfd10184d73760ad23de2f9311'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body = f"Hi {self.p_id.firstname} {self.p_id.lastname} You are discharged from the hospital..Your total bill amount is{self.Total_charge}",
                from_='+19703663980',
                to='+919605660774')
            print(message.sid)
            return super().save(*args,**kwargs)

