from rest_framework import serializers
from customers.models import Customer, Email

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('address', 'description')

class CustomerSerializer(serializers.ModelSerializer):
    emails = EmailSerializer(many=True)
    class Meta:
        model = Customer
        fields = ('id', 'name', 'date_of_birth', 'gender', 'emails')

    def create(self, validated_data):
        emails = validated_data.pop('emails')        
        customer = Customer.objects.create(**validated_data)
        for email in emails:
            Email.objects.create(customer=customer,**email)
        return customer

    def validate_emails(self, value):
        if not value:
            raise serializers.ValidationError('Must have at least one e-mail');
        
        if self.any_duplicate(value):
            raise serializers.ValidationError('Duplicated e-mails are not valid');

        return value

    def any_duplicate(self, email_list):        
        seen = set()
        for email in email_list:
            if email['address'] in seen: return True
            seen.add(email['address'])
        return False

'''
POST example:
{
    "name": "Multiple emails",
    "date_of_birth": "2001-10-01",
    "gender": "M",
    "emails": [
       {"address": "guilhermelatrova@hotmail.com", "description": "Main"},
       {"address": "guilhermelatrova@gmail.com", "description": "Google"}       
]
}
'''