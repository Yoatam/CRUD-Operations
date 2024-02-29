from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()


    def __str__(self):
        return self.name
    
class Address(models.Model):
     street = models.CharField(max_length=100)
     city = models.CharField(max_length=50)
     country = models.CharField(max_length=50)

     def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"
    
