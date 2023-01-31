from django.shortcuts import redirect, render
from .forms import CardsForm
from .models import Cards


def index(request):
    us = request.user
    cards = Cards.objects.all()
    res = []
    for i in cards:
        t = i.coo
        res.append(int(t * 5))
    return render(request, 'exort/index.html', {"cards": cards, "us": us, "res": res})

def food(request):
    us = request.user

    cards = Cards.objects.all()
    return render(request, 'exort/food.html', {"cards": cards, 'us': us})

def place(request):
    us = request.user

    cards = Cards.objects.all()
    return render(request, 'exort/place.html', {"cards": cards, 'us': us})

def create_card(request):
    us = request.user

    error = ''
    if request.method == "POST":
        form = CardsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена некоректно'

    form = CardsForm()

    data = {
        'form': form,
        'error': error,
        'us': us
    }

    return render(request, 'exort/create_card.html', data)