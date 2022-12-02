from django.db import models
from deck.models import PublicFlashcardDeck, PrivateFlashcardDeck

class PublicFlashcard(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    deck = models.ForeignKey(PublicFlashcardDeck, on_delete=models.CASCADE)

class PrivateFlashcard(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    srsLevel = models.IntegerField(default=0)
    # nextReviewDate
    deck = models.ForeignKey(PrivateFlashcardDeck, on_delete=models.CASCADE)
    