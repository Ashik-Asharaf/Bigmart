from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Message = models.CharField(max_length=500,null=True,blank=True)

class CartDb(models.Model):
    Uname = models.CharField(max_length=100,null=True,blank=True)
    Pname = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Total = models.IntegerField(null=True,blank=True)


class RegDb(models.Model):
    RaName = models.CharField(max_length=100,null=True,blank=True)
    RaEmail = models.EmailField(max_length=100,null=True,blank=True)
    RPassword = models.CharField(max_length=100,null=True,blank=True)