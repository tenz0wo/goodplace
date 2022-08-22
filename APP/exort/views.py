from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib import messages

from .forms import CardsForm, CreateUserForm
from .models import Cards


def index(request):
    cards = Cards.objects.all()
    return render(request, 'exort/index.html', {"cards": cards})

def food(request):
    cards = Cards.objects.all()
    return render(request, 'exort/food.html', {"cards": cards})

def place(request):
    cards = Cards.objects.all()
    return render(request, 'exort/place.html', {"cards": cards})

def create_card(request):
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
        'error': error
    }

    return render(request, 'exort/create_card.html', data)





  