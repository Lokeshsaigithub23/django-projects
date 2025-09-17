import os
os.environ.setdefault('DJANGO_SETTING_MODULE','modelproject3.settings')
import django
django.setup()
from faker import Faker
from random import *
from testapp.models import student
faker=Faker()
def phonenumbergrn():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        frollno=faker.random_int(min=1,max=999)
        fname=faker.name()
        fdob=faker.date()
        fmarks=faker.random_int(min=1,max=100)
        fphonenumber=phonenumbergen()
        faddresss=faker.address()
student.objects.get_or_create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddress)        
n=int(input('enter number of records'))
populate(n)
print(f'{n}records inserted successfull')

       