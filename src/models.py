from django.db import models

# Create your models here.


class Coffee(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)
    