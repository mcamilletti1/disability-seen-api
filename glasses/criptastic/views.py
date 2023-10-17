from rest_framework import generics
from .models import Cast, Movie, Review
from .serializers import CastSerializer, MovieSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly

class CastListCreate(generics.ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class CastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]