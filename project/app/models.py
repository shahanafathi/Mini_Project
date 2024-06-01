from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomeUser(AbstractUser):
    age=models.IntegerField(null=True,blank=True)
    Phonenumber=models.IntegerField(null=True,blank=True,unique=True)
    Address=models.CharField(null=True,blank=True,max_length=100)
    DOB=models.DateField(default='2000-01-01')
    InitialAmount=models.IntegerField(null=True,blank=True)
    AccountNumber=models.CharField(null=True,blank=True,max_length=100,unique=True)
    Pancardno=models.CharField(null=True,blank=True,max_length=100,unique=True)
    AdharNumber=models.CharField(null=True,blank=True,max_length=100,unique=True)
    Ifsc=models.IntegerField(null=True,blank=True)
    Branch=models.CharField(null=True,blank=True ,max_length=100)
    Pincode=models.IntegerField(null=True,blank=True)
    usertype=models.CharField(max_length=200)
    Image=models.FileField(null=True,blank=True)
    def __str__(self):
        return self.usertype
    
class transaction(models.Model):
    user_id = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    details=models.CharField(null=True,blank=True,max_length=200)
    amount=models.IntegerField(null=True,blank=True)
    balance=models.IntegerField(null=True,blank=True)
    dateandtime = models.DateTimeField(auto_now_add=True)
    

    