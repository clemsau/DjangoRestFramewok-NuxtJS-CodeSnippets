from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SnippetsViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetsViewSet)

urlpatterns = [
    path("", include(router.urls))
]
