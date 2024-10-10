from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet, CollectionViewSet


router = DefaultRouter()
router.register(r'links', LinkViewSet, basename='link')
router.register(r'collections', CollectionViewSet, basename='collection')

urlpatterns = [
    path('', include(router.urls)),
]
