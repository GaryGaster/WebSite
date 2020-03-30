# Generated by Django 3.0.2 on 2020-03-20 16:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20200319_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='anime_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='movie_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='serial',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='serial_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='xvideo',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='xvideo_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
