from django.shortcuts import render
from .models import Movie, Category
from django.views.generic.base import View


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movie_list': movies})


class CategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'category/category.html', {'category_list': category})
