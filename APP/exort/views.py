from django.shortcuts import redirect, render
from django.views.generic import DeleteView, UpdateView
from .forms import CardsForm, RatingForm
from .models import Cards


class PostUpdateView(UpdateView):
    model = Cards
    template_name = 'exort/create_card.html' 
    form_class = CardsForm

class PostDeleteView(DeleteView):
    model = Cards
    template_name = 'exort/card-delete.html' 
    success_url = '/'

def index(request):
    us = request.user
    cards = Cards.objects.all()
    post_count = Cards.objects.count()

    star_form = RatingForm()
    data = {"cards": cards, 
            "us": us,
            "star_form": star_form,
            'post_count': post_count
            }
    return render(request, 'exort/cards_list.html', data)

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