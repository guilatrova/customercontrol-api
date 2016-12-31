from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from customers.models import Customer
from customers.serializers import CustomerSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer