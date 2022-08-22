from django.db import models

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


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Где поесть или куда сходить'
        verbose_name_plural = 'Места' 
