from django.conf import settings
from django.db import models


class Product(models.Model):
    "Generated Model"
    name = models.TextField()
    price = models.BigIntegerField(
        null=True,
        blank=True,
    )
