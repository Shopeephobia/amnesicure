from django.contrib import admin
from deck.models import PrivateFlashcardDeck, PublicFlashcardDeck

admin.site.register(PrivateFlashcardDeck)
admin.site.register(PublicFlashcardDeck)