from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Client(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = PhoneNumberField(region='IN')
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="inactive")

    def __str__(self):
        return self.fullname
