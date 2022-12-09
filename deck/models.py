from django.db import models
from django.contrib.auth.models import User

class PrivateFlashcardDeck(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PublicFlashcardDeck(models.Model):
    name = models.TextField()

class PublishPrivateDeck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    private_deck = models.ForeignKey(PrivateFlashcardDeck, on_delete=models.CASCADE)
    public_deck = models.ForeignKey(PublicFlashcardDeck, on_delete=models.CASCADE)
    isVerified = models.BooleanField(default=False)