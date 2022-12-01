from django.contrib import admin
from .models import PrivateFlashcard, PublicFlashcard

admin.site.register(PrivateFlashcard)
admin.site.register(PublicFlashcard)