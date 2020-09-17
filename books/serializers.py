from rest_framework import serializers

import books.models as models

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ['name', 'surname', 'age', 'image', 'about']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['name', 'author', 'image', 'about']