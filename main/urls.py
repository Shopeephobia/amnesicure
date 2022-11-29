from django.urls import include, path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
]