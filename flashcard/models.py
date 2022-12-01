from django.db import models

class FlashCard(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    