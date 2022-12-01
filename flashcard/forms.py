from django.forms import ModelForm
from .models import FlashCard


class FlashCardForm(ModelForm):
    class Meta:
        model = FlashCard
        fields=['question', 'answer']