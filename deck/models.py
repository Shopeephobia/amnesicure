from django.db import models
from django.contrib.auth.models import User

class PrivateFlashcardDeck(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PublicFlashcardDeck(models.Model):
    name = models.TextField()