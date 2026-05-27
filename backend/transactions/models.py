from django.db import models

# Create your models here.
from django.db import models


class Transaction(models.Model):

    TRANSACTION_TYPES = (
        ('UPI', 'UPI'),
        ('CARD', 'CARD'),
        ('BANK', 'BANK'),
    )

    transaction_id = models.CharField(max_length=100, unique=True)

    sender_name = models.CharField(max_length=100)

    receiver_name = models.CharField(max_length=100)

    amount = models.FloatField()

    transaction_type = models.CharField(
        max_length=20,
        choices=TRANSACTION_TYPES
    )

    location = models.CharField(max_length=100)

    device_id = models.CharField(max_length=200)

    ip_address = models.GenericIPAddressField()

    timestamp = models.DateTimeField(auto_now_add=True)

    is_fraud = models.BooleanField(default=False)

    fraud_score = models.FloatField(default=0.0)

    def __str__(self):
        return self.transaction_id