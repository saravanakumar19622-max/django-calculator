from django.urls import path
from .views import *

urlpatterns = [
   path('', index, name='index'),
    path('about/', about, name='about'),
    path('calculate/', calculate, name='calculate'),
    path('contact/', contact, name='contact'),
    path('calculation-history/', calculation_history, name='calculation_history'),
   path('health/', health, name='health'),
    # Add other URL patterns as needed
]