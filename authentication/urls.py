from django.urls import include, path
from .views import index, json_data, logoutUser, cekLogin
from .views import loginPage
from .views import daftarPage

urlpatterns = [
    path('', index, name='index'),
    path('login', loginPage, name='login'),
    path('daftar', daftarPage, name='daftar'),
    path('logout', logoutUser, name='logout'),
    path('json',json_data, name='json'),
]