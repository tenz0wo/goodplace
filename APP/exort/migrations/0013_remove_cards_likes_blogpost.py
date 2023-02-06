# Generated by Django 4.2a1 on 2023-02-06 06:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exort', '0012_cards_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='likes',
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.ManyToManyField(related_name='blogpost_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
