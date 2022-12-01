from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from deck.models import PrivateFlashcardDeck
from deck.forms import DeckForm

def deck_index(request):
    decks = PrivateFlashcardDeck.objects.all
    return render(request,'deck_list.html',{'decks': decks})

def create_deck(request):
    form = DeckForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':

        deck_data = form.save(commit=False)

        deck_data.user = request.user
        
        deck_data.save()

        return HttpResponseRedirect(reverse('deck:index'))

    context = {'form':form}

    return render(request, 'deck_form.html', context)