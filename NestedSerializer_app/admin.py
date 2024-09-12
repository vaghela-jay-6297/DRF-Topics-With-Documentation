from django.contrib import admin
from NestedSerializer_app.models import Author, Book, Musician, Album

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'subject')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'release_data', 'rating')

class MusicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'instrument')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'release_data', 'rating', 'artist')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)