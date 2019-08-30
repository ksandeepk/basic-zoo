from django.db import models

# Create your models here.
class areg(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=20)

class booking(models.Model):
    ticket_id=models.CharField(max_length=20)
    name=models.CharField(max_length=30)
    vage=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10) 
    country=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    id_proof=models.CharField(max_length=30)
    id_number=models.CharField(max_length=30)
    vtotal=models.CharField(max_length=10)
    vehical_no=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    time=models.CharField(max_length=30)