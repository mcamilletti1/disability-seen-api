from rest_framework import generics
from rest_framework.exceptions import NotFound
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
    
class CastMembersByMovie(generics.ListAPIView):
    serializer_class = CastSerializer
    
    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            raise NotFound(detail="Movie not found", code=404)
        return movie.cast_members.all()
    
class ReviewsByMovie(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            raise NotFound(detail="Movie not found", code=404)
        return Review.objects.filter(movie=movie)