from django.contrib import admin
from .models import Cards, UserCardRelation, Rating, RatingStar

admin.site.register(Cards)
admin.site.register(UserCardRelation)
admin.site.register(RatingStar)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "movie", "ip")

