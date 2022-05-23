from django.contrib import admin
from .models import Category, Actor, RatingStar, Rating, Reviews, Genre, MovieShots, Movie


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
