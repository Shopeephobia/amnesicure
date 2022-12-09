from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from deck.models import PrivateFlashcardDeck, PublicFlashcardDeck, PublishPrivateDeck
from deck.forms import DeckForm
from flashcard.models import PrivateFlashcard, PublicFlashcard

@login_required(login_url="auth:login")
def deck_index(request):
    decks = PrivateFlashcardDeck.objects.filter(user=request.user)
    return render(request,'deck_list.html',{'decks': decks})

@login_required(login_url="auth:login")
def create_deck(request):
    form = DeckForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':

        deck_data = form.save(commit=False)
        deck_data.user = request.user
        deck_data.save()

        return HttpResponseRedirect(reverse('deck:index'))

    context = {'form':form}

    return render(request, 'deck_form.html', context)

def fetch_public_deck(request):
    public_decks = PublishPrivateDeck.objects.filter(isVerified = True)
    return render(request,'public_list.html',{'public_decks': public_decks})

@login_required(login_url="auth:login")
def fetch_request_private(request):
    requests = PublishPrivateDeck.objects.filter(user=request.user)
    return render(request,'request_private_list.html',{'requests': requests})

@login_required(login_url="auth:login")
def create_request(request, pk):
    private_deck = PrivateFlashcardDeck.objects.get(pk=pk)
    public_deck = None

    # Check if the deck is already published
    try:
        public_deck = PublishPrivateDeck.objects.get(private_deck=private_deck)
        message = 'Request sudah pernah dibuat sebelumnya'
        decks = PrivateFlashcardDeck.objects.filter(user=request.user)
        return render(request,'deck_list.html',{'decks': decks, 'message': message})

    except PublishPrivateDeck.DoesNotExist: 
        deck_request = PublishPrivateDeck(user=request.user, private_deck=private_deck, public_deck=public_deck, isVerified=False)
        deck_request.save()

    message = 'Request berhasil dibuat'
    decks = PrivateFlashcardDeck.objects.filter(user=request.user)
    return render(request,'deck_list.html',{'decks': decks, 'message': message})

@login_required(login_url="auth:login")
def fetch_requests(request):
    if request.user.is_superuser:
        requests = PublishPrivateDeck.objects.filter(isVerified = False)

        return render(request,'request_list.html',{'requests': requests})
    return HttpResponseForbidden()

@login_required(login_url="auth:login")
def verify_request(request, pk):
    if request.user.is_superuser:
        pub_deck = PublishPrivateDeck.objects.get(pk=pk)
        pub_deck.isVerified = True
        pub_deck.public_deck = PublicFlashcardDeck(name=pub_deck.private_deck.name)
        card_list = PrivateFlashcard.objects.filter(deck=pub_deck.private_deck)
        pub_deck.public_deck.save()
        pub_deck.save()
        
        for card in card_list:
            new_pub_card = PublicFlashcard(question=card.question, answer=card.answer, deck=pub_deck.public_deck)
            new_pub_card.save()


        requests = PublishPrivateDeck.objects.filter(isVerified = False)
        message = 'Request berhasil diverifikasi'
        return render(request,'request_list.html',{'requests': requests,'message': message})
    return HttpResponseForbidden()

@login_required(login_url="auth:login")
def reject_request(request, pk):
    if request.user.is_superuser:
        pub_deck = PublishPrivateDeck.objects.get(pk=pk)
        pub_deck.delete()

        requests = PublishPrivateDeck.objects.filter(isVerified = False)
        message = 'Request berhasil ditolak'
        return render(request,'request_list.html',{'requests': requests,'message': message})
    return HttpResponseForbidden()