from django.db import models
from django_countries.fields import CountryField


class Shop(models.Model):
    name = models.CharField(max_length=20)
    founder = models.CharField(max_length=35)
    email = models.CharField(max_length=40)
    country = CountryField()
    salary = models.IntegerField(default=0)
    text = models.CharField(max_length=60, blank=True, null=True)


# shop_list = Shop.objects.filter(id__gt=3)
