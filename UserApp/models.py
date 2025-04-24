from django.db import models

# Create your models here.
class user_registerDB(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirmpwd = models.CharField(max_length=100, null=True, blank=True)