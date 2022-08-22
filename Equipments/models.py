from django.db import models


# Create your models here.

class Equipments(models.Model):
    code = models.CharField(primary_key=True, max_length=12)
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
