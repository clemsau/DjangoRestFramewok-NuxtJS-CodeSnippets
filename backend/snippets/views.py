from rest_framework import viewsets

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetsViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
