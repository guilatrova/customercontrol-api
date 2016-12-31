import django

django.setup()

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from customers.models import Customer, Email

class CustomersTest(APITestCase, TestCase):
    def test_api_should_accept_multiple_emails_for_new_customers(self):
        customer = self.get_default_customer()
        customer['emails'].append({
                "address": "jhondoe@stackoverflow.com",
                "description": "Professional"
            })
        customer['emails'].append({
                "address": "jhondoe@proto.io",
                "description": "Personal"
            })

        response = self.client.post('/api/customers', customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Email.objects.count(), 2)

    def test_api_should_not_accept_empty_email(self):
        customer = self.get_default_customer()

        response = self.client.post('/api/customers', customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_should_not_accept_equal_emails(self):
        customer = self.get_default_customer()
        customer['emails'].append({
                "address": "jhondoe@stackoverflow.com",
                "description": "Professional"
            })
        customer['emails'].append({
                "address": "jhondoe@stackoverflow.com",
                "description": "Personal"
            })

        response = self.client.post('/api/customers', customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def get_default_customer(self):
        return {
            "name": "Jhon Doe",
            "date_of_birth": "1990-3-3",
            "gender": "M",
            "emails": []
        };