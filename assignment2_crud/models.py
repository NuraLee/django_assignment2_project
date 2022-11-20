from django.db import models

# Create your models here.
class Country(models.Model):
    countryName = models.CharField(max_length=50)
    population = models.CharField(max_length=10)
    
    def __str__(self):
        return self.countryName



class Users(models.Model):
    email = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)