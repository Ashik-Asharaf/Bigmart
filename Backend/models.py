from django.db import models

# Create your models here.
class Bigdb(models.Model):
    Cname = models.CharField(max_length=100,null=True,blank=True)
    Description = models.TextField(null=True,blank=True)
    Image=models.ImageField(upload_to="Image",null=True,blank=True)

class ProductDB(models.Model):
    Category = models.CharField(max_length=100,null=True,blank=True)
    ProductName = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=499,null=True,blank=True)
    ProductImage = models.ImageField(upload_to="Product Image",null=True,blank=True)

