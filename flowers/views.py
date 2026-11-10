from django.shortcuts import render
from django.http import HttpResponse


def welcome_view(request):
    return HttpResponse("Witaj w Katalogu Kwiatów!")


def about_view(request):
    return HttpResponse(
        "Katalog Kwiatów pozwala przeglądać kwiaty, ich kategorie, kolory "
        "i porady pielęgnacyjne oraz wystawiać im opinie."
    )