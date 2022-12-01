from django.urls import path
from flashcard.views import *

urlpatterns = [
    path("", list_flashcard, name="card-list"),
    path('add-flashcard', form_flashcard, name='add_flashcard'),
]