from django.urls import path
from .views import MovieListCreate, MovieDetail, CastListCreate, CastDetail, ReviewListCreate, ReviewDetail

urlpatterns = [
    path('movies/', MovieListCreate.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),

    path('casts/', CastListCreate.as_view(), name='cast-list-create'),
    path('casts/<int:pk>/', CastDetail.as_view(), name='cast-detail'),

    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]