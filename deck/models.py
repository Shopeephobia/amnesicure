from django.db import models
from django.contrib.auth.models import User

class PrivateFlashcardDeck(models.Model):
    # String id should be assigned by default in Django
    name = models.TextField()
    # List<PrivateFlashcard> flashcards
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PublicFlashcardDeck(models.Model):
    # String id should be assigned by default in Django
    name = models.TextField()
    # List<PrivateFlashcard> flashcards