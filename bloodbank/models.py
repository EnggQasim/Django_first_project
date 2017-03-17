from django.db import models

# Create your models here.
class Donors(models.Model):
    name=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    bloodGroup=models.CharField(max_length=255)
    donor=models.BooleanField(default=False)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
