import random

from django.core import serializers
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from flashcard.forms import FlashCardForm
from django.contrib.auth.decorators import login_required
from .models import FlashCard

def list_flashcard(request):
    list_flashcard = FlashCard.objects.all
    return render(request,'flashcard_list.html',{'list_flashcard':list_flashcard})

def add_flashcard(request):
    if request.method == 'POST':
        form = FlashCardForm(request.POST)
        if form.is_valid():
            flashcard_form = form.save(commit=False)
            # flashcard_form.user = request.user
            flashcard_form.save()
            return response.HttpResponseRedirect('/')

    else:
        form = FlashCardForm()

    
    return render(request, 'flashcard_form.html', {'form':form})