from django.db import models
from flashcard.models import PrivateFlashcard
import datetime

# Create your models here.
class SRSReview():
    __flashcards:list[PrivateFlashcard] = []
    
    def __init__(self):
        self.__validUntil = datetime.datetime.now() + datetime.timedelta(minutes=10)

    def addFlashcard(self, flashcard: PrivateFlashcard):
        self.__flashcards.append(flashcard)

    def removeFlashcard(self):
        self.__flashcards.pop(0)

    def getFlashcards(self) -> list[PrivateFlashcard]:
        return self.__flashcards

    def isValid(self) -> bool:
        if (datetime.datetime.now() < self.__validUntil):
            return True
        return False

    def extendValidTime(self):
        self.__validUntil = datetime.datetime.now() + datetime.timedelta(minutes=10)

    def answerFlashcard(self, flashcard: PrivateFlashcard, isCorrect: bool):
        self.extendValidTime()

        if isCorrect == True:
            flashcard.srsLevel = min(flashcard.srsLevel+1, 4)
        else:
            flashcard.srsLevel = max(flashcard.srsLevel-1, 1)
        flashcard.nextReviewDate = datetime.datetime.now + datetime.timedelta(hours=(1 << flashcard.srsLevel))
        flashcard.save()
        
        self.removeFlashcard()



