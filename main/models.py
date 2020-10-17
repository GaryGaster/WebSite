from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import date
from multiselectfield import MultiSelectField



class Video(models.Model):
    PLATFORMS = {
        (1, 'HBO'),
        (2, 'NETFLIX'),
        (3, 'AMAZONPRIME'),
        (4, 'YOUTUBE'),
        (5, 'CDA'),
    }

    GENRES = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
    }

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')
    year = models.IntegerField(null=True, blank=True)
    platforms = MultiSelectField(null=True, blank=True, choices=PLATFORMS)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    votes_total = models.IntegerField(default=0)
    voters = models.ManyToManyField(User, related_name='video_voters')
    image = models.ImageField(null=True, blank=True, default='video-default.jpg', upload_to='media/')
    url = models.URLField(blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRES)

    def __str__(self):
        return self.title

    def title_year(self):
        return self.title + " (" + str(self.year) + ") "

    def timestamp_pretty(self):
        return self.timestamp.strftime('%-H:%M; %d.%m.%Yr.')

    def updated_pretty(self):
        return self.updated.strftime('%-H:%M %d.%m.%Yr.')

    class Meta:
        abstract = True

class Actor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    year_of_birth = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='video-default.jpg', upload_to='media/')
    rating = models.IntegerField(choices=[(i, i) for i in range(0, 11)], blank=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def calculate_age(self):
        today = date.today()
        age = today.year - self.year_of_birth
        return age

    def get_absolute_url(self):
        return reverse('actor-detail', kwargs={'pk': self.pk})



class Movie(Video):
    voters = models.ManyToManyField(User, related_name='movie_voters')
    actors = models.ManyToManyField(Actor, blank=True)

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})


class Serial(Video):
    voters = models.ManyToManyField(User, related_name='serial_voters')
    actors = models.ManyToManyField(Actor, blank=True)

    def get_absolute_url(self):
        return reverse('serial-detail', kwargs={'pk': self.pk})


class Anime(Video):
    voters = models.ManyToManyField(User, related_name='anime_voters')
    actors = models.ManyToManyField(Actor, blank=True)

    def get_absolute_url(self):
        return reverse('anime-detail', kwargs={'pk': self.pk})


class MovieRating(models.Model):
    review = models.TextField(default='')
    rating = models.PositiveSmallIntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class SerialRating(models.Model):
    review = models.TextField(default='')
    rating = models.PositiveSmallIntegerField(default=5)
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)


class AnimeRating(models.Model):
    review = models.TextField(default='')
    rating = models.PositiveSmallIntegerField(default=5)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)