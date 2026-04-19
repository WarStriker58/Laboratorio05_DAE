from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    Un ViewSet que proporciona las operaciones CRUD completas para Movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer