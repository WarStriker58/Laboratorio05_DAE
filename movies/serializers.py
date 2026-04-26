from rest_framework import serializers
from .models import Movie, Genre

# NUEVO
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    # CAMBIO: representar géneros dentro del Movie
    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        required=False,
        help_text="Lista de IDs de géneros"
    )

    class Meta:
        model = Movie
        fields = "__all__"

    # NUEVO
    def create(self, validated_data):
        genre_ids = validated_data.pop("genre_ids", [])
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genre_ids)
        return movie

    # NUEVO
    def update(self, instance, validated_data):
        genre_ids = validated_data.pop("genre_ids", None)
        movie = super().update(instance, validated_data)
        if genre_ids is not None:
            movie.genres.set(genre_ids)
        return movie