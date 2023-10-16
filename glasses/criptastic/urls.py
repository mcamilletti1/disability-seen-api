from django.urls import path
from . import views

urlpatterns = [
    path('api/cast/', views.CastListCreate.as_view() ),
    path('api/movie/', views.MovieListCreate.as_view() ),
    path('api/review/', views.ReviewListCreate.as_view() ),
]