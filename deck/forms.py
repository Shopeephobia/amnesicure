from django.forms import ModelForm
from deck.models import PrivateFlashcardDeck

class DeckForm(ModelForm):
    class Meta:
        model = PrivateFlashcardDeck
        fields = ['name']