from django.db import models

# Create your models here.

class deatilescustomer(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.IntegerField(max_length=100, null=True, blank=True)
    confirmpassword=models.IntegerField(max_length=100, null=True, blank=True)
