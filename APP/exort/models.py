from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = [
    ('Еда', 'Еда'),
    ('Места', 'Места'),
]   


class Cards(models.Model):
    title = models.CharField('Название', max_length=50, null=False) 
    category = models.CharField("Категория", max_length=100, blank=True, null=False, choices=CATEGORY_CHOICES) 
    description = models.TextField('Описание', null=False) 
    city = models.CharField('Город', max_length=50, null=False) 
    image = models.URLField('Избражение', null=False, blank=True) 
    link = models.CharField('Адрес', max_length=50, null=False) 
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_card', default=User)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name = 'Где поесть или куда сходить'
        verbose_name_plural = 'Места' 

class UserCardRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cards = models.ForeignKey(Cards, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}, {self.cards}, {self.like}'


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга' 
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(Cards, on_delete=models.CASCADE, verbose_name="место")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"