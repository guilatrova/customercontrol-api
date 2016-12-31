from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)

class Email(models.Model):
    customer = models.ForeignKey(Customer, related_name='emails')
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=25)