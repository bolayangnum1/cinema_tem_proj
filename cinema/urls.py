from django.urls import path
from . import views


urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('category/', views.CategoryView.as_view())
]
