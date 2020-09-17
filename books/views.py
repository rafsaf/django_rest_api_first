from django.shortcuts import render

from rest_framework import viewsets

import books.models as models
import books.serializers as serializers

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer



