from django.contrib import admin
from .models import Movie, Genre

# NUEVO
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "rating", "release_date")
    search_fields = ("title",)
    list_filter = ("genres", "release_date")  # NUEVO