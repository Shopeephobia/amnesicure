from django.urls import path
from deck.views import deck_index, create_deck, fetch_public_deck, fetch_requests, create_request, verify_request, reject_request

app_name = "deck"

urlpatterns = [
    path('', deck_index, name='index'),
    path('new', create_deck, name='create_deck'),
    path('admin/requests', fetch_requests, name='fetch_requests'),
    path('admin/requests/verify/<id>', verify_request, name='verify_deck'),
    path('admin/requests/reject/<id>', reject_request, name='reject_deck'),
]