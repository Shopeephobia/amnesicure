from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from flashcard.models import PrivateFlashcard
from deck.models import PrivateFlashcardDeck
from .models import SRSReview
import datetime
from json import dumps

reviewSessions:dict[int, SRSReview] = {}

# Create your views here.
@login_required(login_url="login")
def index(request):
    flashcards = []
    isPrevSession = False
    
    if (request.user.id in reviewSessions.keys() and reviewSessions[request.user.id].isValid()):
        flashcards = reviewSessions[request.user.id].getFlashcards()
        isPrevSession = True
    else:
        decks = list(PrivateFlashcardDeck.objects.filter(user=request.user))
        for deck in decks:
            temp_flashcards = PrivateFlashcard.objects.filter(deck=deck).filter(nextReviewDate__lte=datetime.datetime.now)
            flashcards.extend(list(temp_flashcards))

    context = {
        'number_of_review' : len(flashcards),
        'is_prev_session' : isPrevSession,
    }

    # TODO: Frontend Implementation
    return None

@login_required(login_url="login")
def start(request):
    flashcards = []
    decks = list(PrivateFlashcardDeck.objects.filter(user=request.user))
    for deck in decks:
        temp_flashcards = PrivateFlashcard.objects.filter(deck=deck).filter(nextReviewDate__lte=datetime.datetime.now)
        flashcards.extend(list(temp_flashcards))

    if (len(flashcards) == 0):
        return redirect("index")

    reviewSessions[request.user.id] = SRSReview()
    for flashcard in flashcards:
        reviewSessions[request.user.id].addFlashcard(flashcard)

    return redirect("review")


@login_required(login_url="login")
def review(request):
    flashcards:list[PrivateFlashcard] = []
    if (request.user.id in reviewSessions.keys() and reviewSessions[request.user.id].isValid()):
        # Continue session
        flashcards = reviewSessions[request.user.id].getFlashcards()
        reviewSessions[request.user.id].extendValidTime()
    else:
        # Redirect to dashboard
        return redirect("index")

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
    return None
    