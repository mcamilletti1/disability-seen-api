from rest_framework import serializers
from . models import *


class CastSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(
        queryset = Movie.objects.all(),
    )

    class Meta:
        model = Cast
        fields = '__all__'


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    cast_members = CastSerializer(
        many=True,
    )

    movie_url = serializers.ModelSerializer.serializer_url_field(
        view_name='movie_detail'
    )

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return Review.objects.create(**validated_data)