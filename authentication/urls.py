from django.urls import include, path
from .views import json_data, logoutUser, loginPage, registerPage, loginCheck

app_name = 'auth'

urlpatterns = [
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('logout', logoutUser, name='logout'),
    path('json',json_data, name='json'),
]