from django.forms import ModelForm
from flashcard.models import PrivateFlashcard

class FlashcardForm(ModelForm):
    class Meta:
        model = PrivateFlashcard
        fields=['question', 'answer']