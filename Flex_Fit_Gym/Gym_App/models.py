from django.db import models

# Create your models here.
class Customer(models.Model):
    Username = models.CharField(max_length=200)
    Email = models.EmailField()
    password = models.CharField(max_length=200)
    phone_Number= models.CharField(max_length=200)
    MemberShip = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Username
