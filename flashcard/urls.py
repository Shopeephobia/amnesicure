from django.urls import path
from flashcard.views import *

urlpatterns = [
    path("", list_flashcard, name="card-list"),
    path('add-flashcard', add_flashcard, name='add_flashcard'),
    # path("new", views.FlashCardCreateView.as_view(), name="card-create"),
    # path("edit/<int:pk>", views.FlashCardUpdateView.as_view(), name="card-update"),
    # path("box/<int:box_num>", views.BoxView.as_view(), name="box"),
]