from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'genres', GenreViewSet, basename='genres')  # NUEVO

urlpatterns = router.urls