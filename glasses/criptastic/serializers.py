from rest_framework import serializers
from .models import Cast, Movie, Review

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'