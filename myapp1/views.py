from django.http import HttpResponse


def zodiac_views(request):
    return HttpResponse('Aries, Taurus, Gemini, Cancer, Leo, Virgo, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces')


def aries(request):
    return HttpResponse('Это знак Овен')


def leo(request):
    return HttpResponse('Это знак Лев')


def taurus(request):
    return HttpResponse('Это знак Телец')


def gemeni(request):
    return HttpResponse('Это знак Близнецы')


def cancer(request):
    return HttpResponse('Это знак Рак')


def virgo(request):
    return HttpResponse('Это знак Дева')


def libra(request):
    return HttpResponse('Это знак Весы')


def scorpio(request):
    return HttpResponse('Это знак Скорпион')


def sagittarius(request):
    return HttpResponse('Это знак Стрелец')


def сapricorn(request):
    return HttpResponse('Это знак Козерог')


def aquarius(request):
    return HttpResponse('Это знак Водолей')


def pisces(request):
    return HttpResponse('Это знак Рыбы')


from myapp1.models import Shop

first_shop = Shop.objects.create(title="First shop")

second_shop = Shop(title="First shop")
second_shop.save()
third_shop = Shop(title="First shop")
third_shop.save()
four_shop = Shop(title="First shop")
four_shop.save()
five_shop = Shop(title="First shop")
five_shop.save()
shop_list = Shop.objects.filter(id__gt=3)
