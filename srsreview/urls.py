from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('start', start, name='start'),
    path('session', review, name='session'),
]