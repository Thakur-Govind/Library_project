from django.shortcuts import render
from django.contrib.auth import get_user_model #user authentication
# Create your views here.
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer,UserSerializer #the serializer classes created
#in serializers.py
'''CRUDing BOOKS'''
class BookAPIView(generics.ListCreateAPIView):#List of all the books
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView): #details of each book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

'''CRUDing Users'''
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
