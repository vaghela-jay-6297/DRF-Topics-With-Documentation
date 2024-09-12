from django.shortcuts import render
from NestedSerializer_app.models import Author, Book, Musician, Album
from NestedSerializer_app.serializer import AuthorSerializer, BookSerializer, MusicianSerializer, AlbumSerializer
from rest_framework import generics

class AuthorListCreateView(generics.ListCreateAPIView): # user can perform create, get list operations on author table
    # in this class we get book info with their author info but we cant update, delete, create book object
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRUDView(generics.RetrieveUpdateDestroyAPIView): # user can perform retrieve, update & delete operations on author table
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):   # user can perform create, get list operations on book table
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRUDView(generics.RetrieveUpdateDestroyAPIView):   # user can perform retrieve, update & delete operations on book table
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MusicianListView(generics.ListAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
     

