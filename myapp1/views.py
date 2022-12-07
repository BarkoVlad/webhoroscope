from django.http import HttpResponse
from myapp1.models import Shop


def zodiac_views(request):
    return HttpResponse('Aries, Taurus, Gemini, Cancer, Leo, Virgo, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces')


def aries(request):
    return HttpResponse('\nЭто знак Овен')


def leo(request):
    return HttpResponse('\nЭто знак Лев')


def taurus(request):
    return HttpResponse('\nЭто знак Телец')


def gemeni(request):
    return HttpResponse('\nЭто знак Близнецы')


def cancer(request):
    return HttpResponse('\nЭто знак Рак')


def virgo(request):
    return HttpResponse('\nЭто знак Дева')


def libra(request):
    return HttpResponse('\nЭто знак Весы')


def scorpio(request):
    return HttpResponse('\nЭто знак Скорпион')


def sagittarius(request):
    return HttpResponse('\nЭто знак Стрелец')


def сapricorn(request):
    return HttpResponse('\nЭто знак Козерог')


def aquarius(request):
    return HttpResponse('\nЭто знак Водолей')


def pisces(request):
    return HttpResponse('\nЭто знак Рыбы')


