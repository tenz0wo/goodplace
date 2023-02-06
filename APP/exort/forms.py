from .models import Cards, RatingStar, Rating
from django.forms import ModelForm, TextInput, Textarea, Select, URLInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CardsForm(ModelForm):
    class Meta:
        model = Cards
        fields = ['title', 'category', 'description', 'city', 'link', 'image'] 

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название карточки"
            }), 

            "category": Select(attrs={
                "class": "form-control",
            }),

            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Описание карточки"
            }),

             "city": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Город"
            }), 

            "link": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите ссылку сайта или адреса"
            }), 

            "image": URLInput(attrs={
                "class": "form-control",
                "placeholder": "Введите ссылку на изображение (Обязательно URL картинки!)"
             })
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)
