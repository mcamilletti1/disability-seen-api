from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CastViewSet, MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'casts', CastViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]