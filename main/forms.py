from django import forms
from .models import Movie, Serial, Anime, Actor


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'platforms', 'image', 'url', 'genre', 'actors']
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'year': 'Rok',
            'platforms': 'Platformy',
            'image': 'Obrazek',
            'url': 'Link',
            'genre': 'Gatunek',
            'actors': 'Aktorzy'
        }


class SerialForm(forms.ModelForm):
    class Meta:
        model = Serial
        fields = ['title', 'description', 'year', 'platforms', 'image', 'url', 'genre', 'actors']
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'year': 'Rok',
            'platforms': 'Platformy',
            'image': 'Obrazek',
            'url': 'Link',
            'genre': 'Gatunek',
            'actors': 'Aktorzy'
        }


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['title', 'description', 'year', 'platforms', 'image', 'url', 'genre', 'actors']
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'year': 'Rok',
            'platforms': 'Platformy',
            'image': 'Obrazek',
            'url': 'Link',
            'genre': 'Gatunek',
            'actors': 'Aktorzy'
        }

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'year_of_birth', 'rating']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'year_of_birth': 'Rok urodzenia',
            'rating': 'Ocena'
        }