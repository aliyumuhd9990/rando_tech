from django.urls import path
from .views import *


app_name = 'core'


urlpatterns = [
    path('', IndexView, name='index'),
    path('about/', AboutView, name='about'),
    path('services/', ServicesView, name='services'),
    path('services/<int:id>/', ServiceDetailView, name='service_detail'),
    path('contact/', ContactView, name='contact'),
    path('privacy/', PrivacyView, name='privacy'),
    path('security/', SecurityView, name='security'),
    path('faq/', FAQView, name='faq'),
    path('ask-question/', AskView, name='ask'),
]