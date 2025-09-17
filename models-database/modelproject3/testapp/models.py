from django.db import models

# Create your models here.
class student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=64)
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
    address=models.TextField()
