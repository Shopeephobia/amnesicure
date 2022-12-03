from django.urls import path
from deck.views import deck_index, create_deck, fetch_public_deck, fetch_requests, create_request, verify_request, reject_request

app_name = "deck"

urlpatterns = [
    path('', deck_index, name='index'),
    path('new', create_deck, name='create_deck'),
    path('public', fetch_public_deck, name='create_deck'),
    path('requests', create_request, name='create_request'),
    path('requests/new/<int:pk>', create_request, name='create_request'),
    path('admin/requests', fetch_requests, name='fetch_requests'),
    path('admin/requests/verify/<int:pk>', verify_request, name='verify_deck'),
    path('admin/requests/reject/<int:pk>', reject_request, name='reject_deck'),
]