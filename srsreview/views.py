from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from flashcard.models import PrivateFlashcard
from deck.models import PrivateFlashcardDeck
from .models import SRSReview
import datetime
from json import dumps
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

reviewSessions:dict[int, SRSReview] = {}

# Create your views here.
@login_required(login_url="auth:login")
def index(request):
    flashcards = []
    isPrevSession = False
    
    if (request.user.id in reviewSessions.keys() and reviewSessions[request.user.id].isValid()):
        flashcards = reviewSessions[request.user.id].getFlashcards()
        isPrevSession = True
    else:
        decks = list(PrivateFlashcardDeck.objects.filter(user=request.user))
        for deck in decks:
            temp_flashcards = PrivateFlashcard.objects.filter(deck=deck).filter(nextReviewDate__lte=datetime.datetime.now())
            flashcards.extend(list(temp_flashcards))

    context = {
        'number_of_review' : len(flashcards),
        'is_prev_session' : isPrevSession,
    }

    # TODO: Frontend Implementation
    return render(request, 'review_dashboard.html', context)

@login_required(login_url="auth:login")
def start(request):
    flashcards = []
    decks = list(PrivateFlashcardDeck.objects.filter(user=request.user))
    for deck in decks:
        temp_flashcards = PrivateFlashcard.objects.filter(deck=deck).filter(nextReviewDate__lte=datetime.datetime.now())
        flashcards.extend(list(temp_flashcards))

    if (len(flashcards) == 0):
        return HttpResponseRedirect(reverse('srsreview:index'))

    reviewSessions[request.user.id] = SRSReview()
    for flashcard in flashcards:
        reviewSessions[request.user.id].addFlashcard(flashcard)

    return HttpResponseRedirect(reverse('srsreview:session'))

@login_required(login_url="auth:login")
@csrf_exempt
def review(request):
    if request.method == 'POST':
        return answerHandler(request)

    flashcards:list[PrivateFlashcard] = []
    if (request.user.id in reviewSessions.keys() and reviewSessions[request.user.id].isValid()):
        # Continue session
        flashcards = reviewSessions[request.user.id].getFlashcards()
        reviewSessions[request.user.id].extendValidTime()
    else:
        # Redirect to dashboard
        return HttpResponseRedirect(reverse('srsreview:index'))

    flashcards_id = []
    flashcards_question = []
    flashcards_answer = []
    for flashcard in flashcards:
        flashcards_id.append(flashcard.pk)
        flashcards_question.append(flashcard.question)
        flashcards_answer.append(flashcard.answer)

    dataDict = {
        'ids' : flashcards_id,
        'questions' : flashcards_question,
        'answers' : flashcards_answer,
    }

    # https://www.geeksforgeeks.org/how-to-pass-data-to-javascript-in-django-framework/
    dataJSON = dumps(dataDict)

    context = {
        'number_of_review' : len(flashcards),
        'data' : dataJSON,
    }

    # TODO: Frontend Implementation
    return render(request, 'review_session.html', context)
    
def answerHandler(request):
    pk = request.POST.get('id', -1)
    answer = request.POST.get('answer', False)

    if (pk != -1):
        flashcard = PrivateFlashcard.objects.get(pk=pk)
        reviewSessions[request.user.id].answerFlashcard(flashcard, answer)
        return JsonResponse({'message':'Success'})
    
    return HttpResponseBadRequest()