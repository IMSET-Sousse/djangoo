# app/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil de mon site !")
