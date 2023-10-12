from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Movie, Cast, Review
from .serializers import MovieSerializer, CastSerializer, ReviewSerializer

class MovieListCreate(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CastListCreate(ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class CastDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

class ReviewListCreate(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer