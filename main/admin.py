from django.contrib import admin
from .models import Movie, Serial, Anime, MovieRating, SerialRating, AnimeRating

admin.site.register(Movie)
admin.site.register(Serial)
admin.site.register(Anime)
admin.site.register(MovieRating)
admin.site.register(SerialRating)
admin.site.register(AnimeRating)
