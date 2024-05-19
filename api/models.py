from django.db import models

# Create your models here.
#Creatre a company model 
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50,choices=(('IT','IT'),('mOBILE_Phones','Mobile 1')))
    added_date = models.DateTimeField(auto_now=True)
    activ = models.BooleanField(default=True)

    def __str__(self):
        return self.name + self.location


#Employee Models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phonneNo = models.CharField(max_length=11)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(('manage','manageR'),('Software','developer')))

    company = models.ForeignKey(Company,on_delete=models.CASCADE)