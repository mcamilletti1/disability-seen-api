from django.urls import path
from . import views
from .views import ReviewList, MovieList, MovieDetail, CastDetail, ReviewDetail, MovieCastList, MovieReviewsList, MovieTypeSearch

urlpatterns = [
    path('reviews/', ReviewList.as_view(), name='review_list'),
    path('movies/', MovieList.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('cast/<int:pk>/', CastDetail.as_view(), name='cast_detail'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    path('movies/<int:pk>/cast/', MovieCastList.as_view(), name='movie-cast-list'),
    path('movies/<int:pk>/reviews/', MovieReviewsList.as_view(), name='movie-reviews-list'),
    path('movies/search/type/<str:movie_type>/', MovieTypeSearch.as_view(), name='movie-type-search'),
]