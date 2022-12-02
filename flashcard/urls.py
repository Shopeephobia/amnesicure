from django.urls import path
from flashcard.views import *

app_name = "flashcard"

urlpatterns = [
    path("<int:pk>", list_flashcard, name="list_flashcard"),
    path("<int:pk>/new", form_flashcard, name='add_flashcard'),
]