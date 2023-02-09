from django.shortcuts import redirect, render
from django.views.generic import DeleteView, UpdateView
from django.contrib.auth.models import User
from .forms import CardsForm
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
    cards = Cards.objects.all()
    post_count = Cards.objects.count()
    data = {"cards": cards, 
            'post_count': post_count,
            }
    return render(request, 'exort/cards_list.html', data)

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
        'error': error,
    }

    return render(request, 'exort/create_card.html', data)