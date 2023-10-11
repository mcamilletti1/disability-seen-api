from django.urls import path
from .views import MovieListCreate, MovieDetail, CastListCreate, CastDetail, ReviewListCreate, ReviewDetail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', MovieListCreate.as_view(), name='movie-list-create'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie-detail'),

    path('casts/', CastListCreate.as_view(), name='cast-list-create'),
    path('casts/<int:pk>/', CastDetail.as_view(), name='cast-detail'),

    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]