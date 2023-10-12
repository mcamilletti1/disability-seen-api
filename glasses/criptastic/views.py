from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter 
from .models import Movie, Cast, Review
from .serializers import MovieSerializer, CastSerializer, ReviewSerializer


class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['media_type']


class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CastList(ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


class CastDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


class ReviewList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MovieCastList(ListAPIView):
    serializer_class = CastSerializer

    def get_queryset(self):
        movie_id = self.kwargs['pk']

        return Cast.objects.filter(movie__id=movie_id)
    
class MovieReviewsList(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.kwargs['pk']

        return Review.objects.filter(movie__id=movie_id)
    

class MovieTypeSearch(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        movie_type = self.kwargs['movie_type']

        return Movie.objects.filter(media_type__iexact=movie_type)
    

