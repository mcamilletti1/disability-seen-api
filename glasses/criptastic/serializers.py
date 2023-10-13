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
    cast_members = CastSerializer(many=True, read_only=False)
    movie_url = serializers.HyperlinkedIdentityField(view_name='criptastic:movie_detail', lookup_field='pk')

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        cast_members_data = validated_data.pop('cast_members', None)  # Remove the cast_members data from the validated data.
        movie = Movie.objects.create(**validated_data)  # Create the movie instance without the cast_members data.

        # If there are cast members, create each one.
        if cast_members_data:
            for cast_member_data in cast_members_data:
                Cast.objects.create(movie=movie, **cast_member_data)

        return movie


class ReviewSerializer(serializers.HyperlinkedModelSerializer):

    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return Review.objects.create(**validated_data)