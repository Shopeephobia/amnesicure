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

def form_flashcard(request):
    form = FlashCardForm()

    if request.method == "POST":
        form = FlashCardForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}

    return render(request, 'flashcard_form.html', context)
