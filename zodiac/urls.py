from django.contrib import admin
from django.urls import path
import myapp1.views
from myapp1.views import aries
from myapp1.views import leo
from myapp1.views import taurus
from myapp1.views import gemeni
from myapp1.views import cancer
from myapp1.views import virgo
from myapp1.views import libra
from myapp1.views import scorpio
from myapp1.views import sagittarius
from myapp1.views import сapricorn
from myapp1.views import aquarius
from myapp1.views import pisces
from myapp1.models import Shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('zodiac/', myapp1.views.zodiac_views),
    path('horoscope/aries', aries),
    path('horoscope/leo', leo),
    path('horoscope/taurus', taurus),
    path('horoscope/gemeni', gemeni),
    path('horoscope/cancer', cancer),
    path('horoscope/virgo', virgo),
    path('horoscope/libra', libra),
    path('horoscope/scorpio', scorpio),
    path('horoscope/sagittarius', sagittarius),
    path('horoscope/сapricorn', сapricorn),
    path('horoscope/aquarius', aquarius),
    path('horoscope/pisces', pisces),
    path('horoscope/Shop', Shop)


]
