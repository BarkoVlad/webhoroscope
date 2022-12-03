from django.contrib import admin

from myapp1.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'founder', 'email', 'country', 'salary']

