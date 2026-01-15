from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Prductmodel(models.Model):

    product_name = models.CharField(max_length=20)

    product_clr = models.CharField(max_length=20)

    prduct_price = models.IntegerField()