import random

from django.core import serializers
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import response
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from flashcard.forms import FlashcardForm
from django.contrib.auth.decorators import login_required
from flashcard.models import PrivateFlashcard
from deck.models import PrivateFlashcardDeck

def list_flashcard(request, pk):
    deck_parent = PrivateFlashcardDeck.objects.get(pk=pk)
    list_flashcard = PrivateFlashcard.objects.filter(deck=deck_parent)

    context = {
        'deck_name': deck_parent.name,
        'deck_pk': pk,
        'list_flashcard': list_flashcard,
    }


    return render(request,'flashcard_list.html',context)

def form_flashcard(request, pk):
    form = FlashcardForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':

        card_data = form.save(commit=False)

        card_data.deck = PrivateFlashcardDeck.objects.get(pk=pk)
        
        card_data.save()

        return HttpResponseRedirect(reverse('flashcard:list_flashcard', kwargs={'pk': pk}))

    context = {'form':form}

    return render(request, 'flashcard_form.html', context)
