from re import A
from django.contrib import admin
from .models import Cards, UserCardRelation

admin.site.register(Cards)
admin.site.register(UserCardRelation)


