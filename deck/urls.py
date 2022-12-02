from django.urls import path
from deck.views import deck_index, create_deck

app_name = "deck"

urlpatterns = [
    path('', deck_index, name='index'),
    path('new', create_deck, name='create_deck'),
]