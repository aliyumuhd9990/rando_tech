from django.urls import path
from .views import *


app_name = 'core'


urlpatterns = [
    path('', IndexView, name='index'),
    path('about/', AboutView, name='about'),
    path('services/', ServicesView, name='services'),
    path('contact/', ContactView, name='contact'),
]