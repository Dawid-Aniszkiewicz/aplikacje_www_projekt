from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Flower


def flower_list(request):
    # pobieram dostepne kwiaty posortowane po nazwie
    flowers = Flower.objects.filter(is_available=True).select_related('category').order_by('name')
    return render(request, 'flowers/flower_list.html', {'flowers': flowers})


def flower_detail(request, slug):
    # szukam kwiatu po slugu, jak nie ma to blad 404
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'flowers/flower_detail.html', {'flower': flower})


def about_view(request):
    return HttpResponse("Katalog kwiatow - projekt na Aplikacje WWW")