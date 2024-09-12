from rest_framework import serializers
from NestedSerializer_app.models import Author, Book, Musician, Album

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    # nested serializer -> # in this class we get book info with their author info but we cant update, delete, create book object
    books_by_author = BookSerializer(read_only=True, many=True)  # only read
    class Meta:
        model = Author
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(read_only=True, many=True)
    class Meta:
        model = Musician
        fields = "__all__"