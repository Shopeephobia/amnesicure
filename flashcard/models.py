from django.db import models

class FlashCard(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question