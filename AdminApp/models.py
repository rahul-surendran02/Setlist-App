from django.db import models

# Create your models here.
class songDB(models.Model):
    song=models.CharField(max_length=200,null=True,blank=True)
    des=models.CharField(max_length=500,null=True,blank=True)

class admin_registerDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirmpwd = models.CharField(max_length=100, null=True, blank=True)
