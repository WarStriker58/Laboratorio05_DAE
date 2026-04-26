from django.db import models

# NUEVO
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    # NUEVO: relación muchos a muchos
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)

    def __str__(self):
        return self.title