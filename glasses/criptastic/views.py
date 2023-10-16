from rest_framework import generics
from .models import Cast, Movie, Review
from .serializers import CastSerializer, MovieSerializer, ReviewSerializer

class CastListCreate(generics.ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer