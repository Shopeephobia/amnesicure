from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from deck.models import PrivateFlashcardDeck, PublicFlashcardDeck, PublishPrivateDeck
from deck.forms import DeckForm

def deck_index(request):
    decks = PrivateFlashcardDeck.objects.filter(user=request.user)
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

def fetch_public_deck(request):
    public_decks = PublicFlashcardDeck.objects.filter(isVerified = True)
    return render(request,'public_list.html',{'public_decks': public_decks})


def create_request(request, pk):
    private_deck = PrivateFlashcardDeck.objects.get(pk=pk)
    public_deck = None

    # Check if the deck is already published
    try:
        public_deck = PublishPrivateDeck.objects.get(private_deck=private_deck)
        response = {
        'msg':  'Request sudah pernah dibuat sebelumnya',
        'id' : 0
            }
        return JsonResponse(response)

    except PublishPrivateDeck.DoesNotExist: 
        deck_request = PublishPrivateDeck(user=request.user, private_deck=private_deck, public_deck=public_deck, isVerified=False)
        deck_request.save()

    response = {
    'msg':  'Request anda berhasil dibuat',
    'id' : 1
        }
    return JsonResponse(response)


def fetch_requests(request):
    if request.user.is_superuser:
        requests = PublishPrivateDeck.objects.filter(isVerified = False)

        return render(request,'request_list.html',{'requests': requests})
    return HttpResponseForbidden()

def verify_request(request, pk):
    if request.user.is_superuser:
        pub_deck = PublishPrivateDeck.objects.get(pk=pk)
        pub_deck.isVerified = True
        pub_deck.public_deck = PublicFlashcardDeck(name=pub_deck.private_deck.name)
        pub_deck.public_deck.save()
        pub_deck.save()

        response = {
        'msg':  'Request berhasil diterima',
        'id' : 1
            }
        return JsonResponse(response)
    return HttpResponseForbidden()

def reject_request(request, pk):
    if request.user.is_superuser:
        pub_deck = PublishPrivateDeck.objects.get(pk=pk)
        pub_deck.delete()
        response = {
        'msg':  'Request berhasil ditolak',
        'id' : 0
            }
        return JsonResponse(response)
    return HttpResponseForbidden()