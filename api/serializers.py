from rest_framework import serializers
from books.models import Book #Book serializers ke liye
from django.contrib.auth import get_user_model#User Authentication

class BookSerializer(serializers.ModelSerializer): #serializes book objects
    class Meta:
        model = Book
        fields = ('title','subtitle','author','isbn')


class UserSerializer(serializers.ModelSerializer): #serializes user objects
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
