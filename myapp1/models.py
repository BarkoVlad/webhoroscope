from django.db import models
from django_countries.fields import CountryField


class Shop(models.Model):
    objects = None
    name = models.CharField(max_length=20, blank=False)
    founder = models.CharField(max_length=35, blank=False)
    email = models.CharField(max_length=40, blank=False)
    country = CountryField()
    salary = models.IntegerField(default=0)
    text = models.CharField(blank=True, null=True)


# shop_list = Shop.objects.filter(id__gt=3)
