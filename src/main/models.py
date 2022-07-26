from django.db import models

class Product(models.Model):
    name = models.TextField(
        null=False,
        unique=True
    )
    price = models.FloatField(
        null=False,
        default=0.0
    )
