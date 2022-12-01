from django import forms
from .models import FlashCard


class FlashCardForm(forms.Form):
    class Meta:
        model = FlashCard
        fields=['question', 'answer']